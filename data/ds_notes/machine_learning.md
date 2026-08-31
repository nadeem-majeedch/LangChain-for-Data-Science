# Machine Learning Fundamentals

## Overview
Machine Learning is a subset of artificial intelligence where systems learn patterns from data to make predictions or decisions without being explicitly programmed.

## Types of Learning

### Supervised Learning
- **Classification**: Predict categorical labels (spam/not spam)
- **Regression**: Predict continuous values (house prices)
- Uses labeled training data

### Unsupervised Learning
- **Clustering**: Group similar data points (customer segments)
- **Dimensionality Reduction**: Reduce features while preserving information
- Uses unlabeled data

### Reinforcement Learning
- Agent learns through trial and error
- Receives rewards/penalties for actions
- Used in game playing, robotics

## Key Algorithms

### Classification
- **Logistic Regression**: Linear model for binary classification
- **Decision Trees**: Tree-based rule learning
- **Random Forest**: Ensemble of decision trees
- **SVM**: Finds optimal decision boundary
- **K-Nearest Neighbors**: Classifies by majority vote of neighbors
- **Naive Bayes**: Probabilistic classifier using Bayes theorem

### Regression
- **Linear Regression**: Fits a line to predict continuous values
- **Ridge/Lasso Regression**: Regularized linear models
- **Polynomial Regression**: Fits non-linear relationships

### Clustering
- **K-Means**: Partitions data into K groups
- **DBSCAN**: Density-based clustering
- **Hierarchical Clustering**: Builds nested clusters

## Model Selection
1. Start with simple models (baseline)
2. Try multiple algorithms
3. Use cross-validation for evaluation
4. Tune hyperparameters with GridSearch or RandomSearch
5. Consider interpretability requirements

## Common Mistakes
1. **Overfitting**: Model memorizes training data instead of learning patterns
2. **Underfitting**: Model is too simple to capture patterns
3. **Data leakage**: Using test data during training
4. **Ignoring class imbalance**: Skewed datasets lead to biased models
5. **Not preprocessing**: Forgetting to scale features or encode categories
