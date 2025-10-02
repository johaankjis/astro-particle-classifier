# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive README.md with full project documentation
- requirements.txt for easy dependency installation
- CONTRIBUTING.md with contribution guidelines
- LICENSE file (MIT License with dataset attribution)
- .gitignore to exclude unnecessary files from version control
- CHANGELOG.md to track project changes

## [0.1.0] - Initial Release

### Added
- Initial Jupyter notebook implementation (`Ray_Predecition_Model_for_a_telescope.ipynb`)
- MAGIC Gamma Telescope dataset (`magic04.data`)
- Implementation of 5 classification models:
  - K-Nearest Neighbors (KNN)
  - Naive Bayes
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Neural Network with hyperparameter tuning
- Data preprocessing with StandardScaler and RandomOverSampler
- Feature distribution visualization
- Model evaluation using classification reports
- Neural network training history visualization

### Features
- Binary classification of gamma rays vs hadrons
- 10 continuous features from Cherenkov radiation patterns
- Dataset split: 60% training, 20% validation, 20% testing
- Class imbalance handling with oversampling
- Comprehensive hyperparameter tuning for neural network:
  - Number of nodes: [16, 32, 64]
  - Dropout probability: [0, 0.2]
  - Learning rate: [0.01, 0.005, 0.001]
  - Batch size: [32, 64, 128]
