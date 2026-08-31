# Model Evaluation Metrics

## Overview
Evaluating model performance is crucial for understanding how well your model generalizes to unseen data.

## Classification Metrics

### Accuracy
- **Definition**: Percentage of correct predictions
- **Formula**: (TP + TN) / (TP + TN + FP + FN)
- **When to use**: Balanced datasets
- **When NOT to use**: Imbalanced datasets (can be misleading)

### Precision
- **Definition**: Accuracy of positive predictions
- **Formula**: TP / (TP + FP)
- **When to use**: When false positives are costly (spam detection)
- **Example**: Of all emails marked as spam, how many are actually spam?

### Recall (Sensitivity)
- **Definition**: Ability to find all positive instances
- **Formula**: TP / (TP + FN)
- **When to use**: When false negatives are costly (disease detection)
- **Example**: Of all actual spam emails, how many did we catch?

### F1 Score
- **Definition**: Harmonic mean of precision and recall
- **Formula**: 2 * (precision * recall) / (precision + recall)
- **When to use**: Imbalanced datasets, need to balance precision and recall
- **Range**: 0 (worst) to 1 (best)

### Confusion Matrix
A table showing predictions vs actual values:
- **True Positives (TP)**: Correctly predicted positive
- **True Negatives (TN)**: Correctly predicted negative
- **False Positives (FP)**: Incorrectly predicted positive (Type I error)
- **False Negatives (FN)**: Incorrectly predicted negative (Type II error)

## Regression Metrics

### Mean Squared Error (MSE)
- Average of squared differences between predicted and actual
- Penalizes large errors more heavily
- Formula: mean((y_pred - y_actual)^2)

### Root Mean Squared Error (RMSE)
- Square root of MSE
- Same units as the target variable
- More interpretable than MSE

### R-squared (R²)
- Proportion of variance explained by the model
- Range: 0 (no explanation) to 1 (perfect explanation)
- Formula: 1 - (SS_res / SS_tot)

## Choosing the Right Metric
| Scenario | Recommended Metric |
|---|---|
| Balanced classification | Accuracy or F1 |
| Imbalanced classification | F1, Precision-Recall AUC |
| Cost of false positives high | Precision |
| Cost of false negatives high | Recall |
| Regression | RMSE, R² |

## Cross-Validation
- Split data into K folds
- Train on K-1 folds, test on 1 fold
- Repeat K times, average results
- More reliable than single train/test split
- Common values: K=5 or K=10

## Model Evaluation Best Practices
1. Always use a test set never seen during training
2. Use stratified splits for imbalanced data
3. Report confidence intervals, not just single numbers
4. Compare against a simple baseline
5. Consider business context when choosing metrics
