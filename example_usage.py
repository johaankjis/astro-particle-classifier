#!/usr/bin/env python3
"""
Example usage script for Astro Particle Classifier

This script demonstrates how to load the MAGIC Gamma Telescope dataset,
preprocess it, and train a simple classifier outside of the Jupyter notebook.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from imblearn.over_sampling import RandomOverSampler


def load_data(filepath="magic04.data"):
    """
    Load the MAGIC Gamma Telescope dataset.
    
    Args:
        filepath (str): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    cols = [
        "fLength", "fWidth", "fSize", "fConc", "fConc1", 
        "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"
    ]
    df = pd.read_csv(filepath, names=cols)
    return df


def preprocess_data(df, test_size=0.2, random_state=42, oversample=True):
    """
    Preprocess the dataset: encode target, split, scale, and optionally oversample.
    
    Args:
        df (pd.DataFrame): Input dataframe
        test_size (float): Proportion of dataset for testing
        random_state (int): Random seed for reproducibility
        oversample (bool): Whether to apply random oversampling
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # Encode class: gamma (g) = 1, hadron (h) = 0
    df["class"] = (df["class"] == "g").astype(int)
    
    # Split features and target
    X = df.drop("class", axis=1).values
    y = df["class"].values
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Handle class imbalance with oversampling (training set only)
    if oversample:
        ros = RandomOverSampler(random_state=random_state)
        X_train, y_train = ros.fit_resample(X_train, y_train)
    
    return X_train, X_test, y_train, y_test


def train_knn_classifier(X_train, y_train, n_neighbors=5):
    """
    Train a K-Nearest Neighbors classifier.
    
    Args:
        X_train: Training features
        y_train: Training labels
        n_neighbors (int): Number of neighbors
        
    Returns:
        Trained KNN model
    """
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on test data.
    
    Args:
        model: Trained classifier
        X_test: Test features
        y_test: Test labels
    """
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Hadron", "Gamma"]))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(cm)
    print("\nInterpretation:")
    print(f"True Negatives (Hadron correctly identified): {cm[0, 0]}")
    print(f"False Positives (Hadron misclassified as Gamma): {cm[0, 1]}")
    print(f"False Negatives (Gamma misclassified as Hadron): {cm[1, 0]}")
    print(f"True Positives (Gamma correctly identified): {cm[1, 1]}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("MAGIC Gamma Telescope Classifier - Example Usage")
    print("=" * 60)
    
    # Load data
    print("\n[1] Loading dataset...")
    df = load_data()
    print(f"Dataset loaded: {len(df)} samples, {len(df.columns)} columns")
    print(f"Class distribution:\n{df['class'].value_counts()}")
    
    # Preprocess data
    print("\n[2] Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(df, oversample=True)
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    print(f"Features: {X_train.shape[1]}")
    
    # Train model
    print("\n[3] Training K-Nearest Neighbors classifier...")
    model = train_knn_classifier(X_train, y_train, n_neighbors=5)
    print("Model trained successfully!")
    
    # Evaluate model
    print("\n[4] Evaluating model on test set...")
    evaluate_model(model, X_test, y_test)
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
