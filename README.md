# Astro Particle Classifier

A machine learning project that classifies gamma ray and hadron events from the MAGIC Gamma Telescope using Cherenkov radiation patterns. This project implements and compares multiple classification algorithms to distinguish between signal (gamma rays) and background (hadron) events.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Models Implemented](#models-implemented)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The MAGIC (Major Atmospheric Gamma Imaging Cherenkov) Telescope is designed to detect gamma rays from cosmic sources. This project uses machine learning techniques to classify whether detected radiation events are gamma rays (signal) or hadrons (background noise).

The classification is based on 10 continuous features derived from the image parameters of the Cherenkov radiation patterns captured by the telescope.

## Dataset

**Source:** UCI Machine Learning Repository - [MAGIC Gamma Telescope Dataset](https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope)

**Description:** 
- Total samples: 19,020
- Features: 10 continuous attributes
- Target: Binary classification (gamma 'g' vs hadron 'h')

### Feature Descriptions

The dataset includes the following features measured from Cherenkov radiation images:

1. **fLength**: Major axis of ellipse (mm)
2. **fWidth**: Minor axis of ellipse (mm)
3. **fSize**: 10-log of sum of content of all pixels (in photo-electrons)
4. **fConc**: Ratio of sum of two highest pixels over fSize
5. **fConc1**: Ratio of highest pixel over fSize
6. **fAsym**: Distance from highest pixel to center, projected onto major axis (mm)
7. **fM3Long**: 3rd root of third moment along major axis (mm)
8. **fM3Trans**: 3rd root of third moment along minor axis (mm)
9. **fAlpha**: Angle of major axis with vector to origin (deg)
10. **fDist**: Distance from origin to center of ellipse (mm)

**Target Variable:**
- `g` (gamma): Signal event
- `h` (hadron): Background event

## Features

- **Data Preprocessing**: StandardScaler normalization and RandomOverSampler for class imbalance
- **Multiple ML Models**: Implementation of 5 different classification algorithms
- **Neural Network Hyperparameter Tuning**: Grid search over multiple parameters
- **Model Comparison**: Performance evaluation using classification metrics
- **Visualization**: Distribution plots for feature analysis

## Models Implemented

The project implements and compares the following machine learning models:

1. **K-Nearest Neighbors (KNN)**
   - Algorithm: Distance-based classification
   - Parameters: k=5 neighbors

2. **Naive Bayes**
   - Algorithm: Gaussian Naive Bayes
   - Probabilistic classifier based on Bayes' theorem

3. **Logistic Regression**
   - Algorithm: Linear classification model
   - Binary classification with sigmoid function

4. **Support Vector Machine (SVM)**
   - Algorithm: Maximum margin classifier
   - Kernel-based classification

5. **Neural Network (Deep Learning)**
   - Framework: TensorFlow/Keras
   - Architecture: Multi-layer perceptron with dropout
   - Hyperparameter tuning across:
     - Number of nodes: [16, 32, 64]
     - Dropout probability: [0, 0.2]
     - Learning rate: [0.01, 0.005, 0.001]
     - Batch size: [32, 64, 128]
   - Epochs: 100
   - Activation: ReLU (hidden layers), Sigmoid (output)
   - Loss: Binary crossentropy

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/johaankjis/astro-particle-classifier.git
cd astro-particle-classifier
```

2. Install required packages:
```bash
pip install numpy pandas matplotlib scikit-learn imbalanced-learn tensorflow
```

## Usage

### Running the Notebook

1. Launch Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `Ray_Predecition_Model_for_a_telescope.ipynb`

3. Run all cells sequentially to:
   - Load and preprocess the data
   - Visualize feature distributions
   - Train multiple models
   - Compare model performances

### Quick Start Example

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Load data
cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", 
        "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols)

# Preprocess
df["class"] = (df["class"] == "g").astype(int)

# Split and scale
# ... (see notebook for complete preprocessing)

# Train model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Predict
predictions = knn_model.predict(X_test)
```

## Project Structure

```
astro-particle-classifier/
├── README.md                                  # Project documentation
├── Ray_Predecition_Model_for_a_telescope.ipynb  # Main Jupyter notebook
└── magic04.data                               # MAGIC Gamma Telescope dataset
```

## Results

The project evaluates all models using standard classification metrics:
- Precision
- Recall
- F1-Score
- Accuracy

The neural network model includes:
- Training/validation loss curves
- Accuracy plots across epochs
- Hyperparameter optimization to find the best configuration

The best performing model is selected based on validation loss and evaluated on the test set.

## Requirements

### Core Dependencies
- **numpy**: Numerical computing
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning algorithms and preprocessing
  - StandardScaler
  - Train/test splitting
  - Classification algorithms (KNN, Naive Bayes, Logistic Regression, SVM)
  - Evaluation metrics
- **imbalanced-learn**: Handling imbalanced datasets (RandomOverSampler)
- **tensorflow**: Deep learning framework for neural network implementation

### Suggested versions:
```
numpy>=1.19.0
pandas>=1.1.0
matplotlib>=3.3.0
scikit-learn>=0.23.0
imbalanced-learn>=0.7.0
tensorflow>=2.3.0
```

## Contributing

Contributions are welcome! Here are some ways you can contribute:

- Implement additional classification algorithms
- Improve hyperparameter tuning strategies
- Add more visualization and analysis
- Optimize model performance
- Improve documentation
- Report bugs or suggest features

Please feel free to open issues or submit pull requests.

## License

This project is available for educational and research purposes. Please cite the original MAGIC Gamma Telescope dataset:

```
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository
[http://archive.ics.uci.edu/ml]. Irvine, CA: University of California,
School of Information and Computer Science.
```

## Acknowledgments

- UCI Machine Learning Repository for providing the MAGIC Gamma Telescope dataset
- The MAGIC Telescope collaboration for collecting and sharing the data
- scikit-learn and TensorFlow communities for excellent machine learning tools

## Contact

For questions or feedback, please open an issue on GitHub.
