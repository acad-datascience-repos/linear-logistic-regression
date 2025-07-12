# Logistic Regression Assignment

## Problem Description

In this assignment, you will train a Logistic Regression model, a fundamental algorithm for binary and multi-class classification. You will use the famous Iris dataset to classify species of iris flowers.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `train_logistic_regression_on_iris()`.
3.  Your tasks are to:
    *   Load the Iris dataset from `sklearn.datasets`.
    *   Split the data into training and testing sets (80% train, 20% test).
    *   Create and train a `LogisticRegression` model.
    *   Make predictions on the test set.
    *   Calculate and return the accuracy of the model.

## Hints

*   Use `load_iris()` to get the data.
*   Use `train_test_split` from `sklearn.model_selection`. Set `random_state=42` for reproducibility.
*   The `LogisticRegression` model is in `sklearn.linear_model`.
*   Use `model.fit()` to train, `model.predict()` to predict, and `accuracy_score` from `sklearn.metrics` to evaluate.

## Further Exploration (Optional)

*   The trained model has an attribute `model.coef_`. What does this attribute represent? How can it tell you about the importance of different features?
*   What is regularization in logistic regression? Look at the `penalty` and `C` parameters of the `LogisticRegression` model.
*   How would you get a confusion matrix for your model's predictions? (Hint: `confusion_matrix` from `sklearn.metrics`)