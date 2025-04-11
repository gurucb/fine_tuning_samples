import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms


class SimpleCNNModel(nn.Module):
    def __init__(self):
        super(SimpleCNNModel, self).__init__()
        self.convnet_layer1 = nn.Conv2d(in_channels=3,out_channels=32,kernel_size=3,stride=1)
        self.convnet_layer2 = nn.Conv2d(in_channels=32,out_channels=32,kernel_size=3)
        self.maxpool_layer1 = nn.MaxPool2d(kernel_size=2,stride=2)

        self.convnet_layer3 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3)
        self.convnet_layer4 = nn.Conv2d(in_channels=64,out_channels=64,kernel_size=3)
        self.maxpool_layer2 = nn.MaxPool2d(kernel_size=2,stride=2)

        self.fully_connected_layer1 = nn.Linear(64*5*5,128)
        self.relu_layer = nn.ReLU()
        self.fully_connected_layer2 = nn.Linear(128,10)

    def forward(self, x):
        out = self.convnet_layer1(x)
        out = self.convnet_layer2(out)
        out = self.maxpool_layer1(out)
        out = self.convnet_layer3(out)
        out = self.convnet_layer4(out)
        out = self.maxpool_layer2(out)
        out = out.view(out.size(0), -1)
        out = self.fully_connected_layer1(out)
        out = self.relu_layer(out)
        out = self.fully_connected_layer2(out)
        return out  

class DataPreprocess:
    def __init__(self):
        self.transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    def get_train_data_loader(self):
        train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=self.transform)
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, shuffle=True, num_workers=2)
        return train_loader

    def get_test_data_loader(self):
        test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=self.transform)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=4, shuffle=False, num_workers=2)
        return test_loader

class ModelTrain:
    def __init__(self):
        self.model = SimpleCNNModel()
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.001, momentum=0.9)
        self.data_preprocess = DataPreprocess()
        self.train_loader = self.data_preprocess.get_train_data_loader()
        self.test_loader = self.data_preprocess.get_test_data_loader()

    def train_model(self):
        for epoch in range(2):
            running_loss = 0.0
            for i, data in enumerate(self.train_loader, 0):
                inputs, labels = data
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
                if i % 2000 == 1999:
                    print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
                    running_loss = 0.0
        print('Finished Training')

    def test_model(self):
        correct = 0
        total = 0
        with torch.no_grad():
            for data in self.test_loader:
                images, labels = data
                outputs = self.model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))


if __name__ == '__main__':
    model_train = ModelTrain()
    model_train.train_model()
    model_train.test_model()