"""
Example script demonstrating the usage of the RandomForestMalwareClassifier.
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from malware_classifier.models.random_forest_classifier import RandomForestMalwareClassifier

def main():
    # Generate synthetic data for demonstration
    print("Generating synthetic malware data...")
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        random_state=42
    )
    
    # Create feature names
    feature_names = [f"feature_{i}" for i in range(X.shape[1])]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\nTraining set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    # Initialize and train the classifier
    print("\nInitializing and training the classifier...")
    classifier = RandomForestMalwareClassifier()
    classifier.fit(X_train, y_train, feature_names=feature_names)
    
    # Make predictions
    print("\nMaking predictions...")
    y_pred = classifier.predict(X_test)
    y_pred_proba = classifier.predict_proba(X_test)
    
    # Calculate accuracy
    accuracy = np.mean(y_pred == y_test)
    print(f"\nAccuracy: {accuracy:.2%}")
    
    # Get feature importance
    print("\nTop 5 most important features:")
    top_features = classifier.get_feature_importance_top_k(k=5)
    for feature, importance in top_features.items():
        print(f"{feature}: {importance:.4f}")

if __name__ == "__main__":
    main() 