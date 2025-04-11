
# Fine Tuning Repo

Welcome to the Fine Tuning Repo! This repository is dedicated to exploring various aspects of fine-tuning machine learning models. As I continue to learn and expand my understanding, this repo will evolve with more content and insights.

## Contents

### 1. PEFT (Performance Efficient Fine-Tuning)
- **Quantization**: Techniques to reduce the precision of the numbers used in model computations, making models faster and more efficient.
- **LoRA (Lower Order Rank Adaptation)**: A method to adapt pre-trained models to new tasks with minimal computational resources.

### 2. Understanding GPU / CPU / TPUs
- Detailed explanations of the differences, advantages, and use cases for GPUs, CPUs, and TPUs in machine learning.

### 3. Data Preparation (Instruction Set)
- Guidelines and best practices for preparing data for fine-tuning, including data cleaning, augmentation, and formatting.

### 4. Fine Tuning
- Step-by-step instructions and methodologies for fine-tuning pre-trained models on new datasets.

### 5. Evaluation
- Techniques and metrics for evaluating the performance of fine-tuned models.

## Repository Contents

This repository contains the following directories and files:

| Type      | Name                       |
|-----------|----------------------------|
| Directory | data_generation            |
| Directory | slm_evaluation             |
| Directory | slm_tuning                 |
| File      | README.md                  |
| File      | deepseek_with_CPU.ipynb    |
| File      | deepseek_with_GPU.ipynb    |
| File      | quantization_samples.ipynb |
| File      | requirements.txt           |
| File      | simple_model.py            |

### Directories
- **data_generation**: Contains scripts and data related to generating datasets.
- **slm_evaluation**: Contains scripts and notebooks for evaluating the SLM (Small Language Model) models.
- **slm_tuning**: Contains scripts and notebooks for tuning the SLM models.

### Files
- **README.md**: Provides an overview of the repository, including setup instructions, usage, and other relevant information.
- **deepseek_with_CPU.ipynb**: Jupyter notebook for running DeepSeek model on CPU.
- **deepseek_with_GPU.ipynb**: Jupyter notebook for running DeepSeek model on GPU.
- **quantization_samples.ipynb**: Jupyter notebook containing examples of model quantization techniques.
- **requirements.txt**: Lists all dependencies required to run the code in this repository.
- **simple_model.py**: Python script defining a simple CNN Model to understand downcasting

## Note
This repository will evolve as I add more content and increase my understanding of each aspect of fine-tuning.

## History
- **April 2025**: Repurposed this repo for internal team training.

Feel free to contribute, raise issues, or suggest improvements. Happy fine-tuning!
