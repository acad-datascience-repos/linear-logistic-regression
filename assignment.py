from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_logistic_regression_on_iris():
  """
  Trains a Logistic Regression model on the Iris dataset and returns its accuracy.

  Returns:
    The accuracy of the model on the test set.
  """
  # Task 1: Load the Iris dataset
  iris = None
  X, y = (None, None)
  # Your code here

  # Task 2: Split the data
  X_train, X_test, y_train, y_test = (None, None, None, None)
  # Your code here

  # Task 3: Create and train the model
  model = None
  # Your code here

  # Task 4: Make predictions and calculate accuracy
  predictions = None
  accuracy = None
  # Your code here

  return accuracy
