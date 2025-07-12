import unittest
from assignment import train_logistic_regression_on_iris

class TestLogisticRegression(unittest.TestCase):
    def test_train_logistic_regression_on_iris(self):
        accuracy = train_logistic_regression_on_iris()
        self.assertIsInstance(accuracy, float)
        # Check for a reasonable accuracy
        self.assertGreater(accuracy, 0.9)

if __name__ == '__main__':
    unittest.main()
