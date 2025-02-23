# Logistic Regression from Scratch

## Overview
This project implements Logistic Regression from scratch using Python. The goal is to understand and implement the core mathematical concepts behind logistic regression without relying on high-level libraries like Scikit-Learn.

## Folder Structure
```
LogisticRegression/
│── Logistic_Regression.pdf (Concept Notes and Mathematical Derivation)
│── LogisticRegression.py (Implementation of the Logistic Regression class)
│── diabetes.csv (Dataset used for testing, sourced from Kaggle)
│── main.py (Testing and running the Logistic Regression model)
```

## Dataset
The dataset used (`diabetes.csv`) is sourced from Kaggle Open Datasets:
[Diabetes Dataset](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset)

## Mathematical Foundation
The theoretical derivation of Logistic Regression used in this project is based on the following references:
- [Logistic Regression Clearly Explained by StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)

## Implementation Details
- The `LogisticRegression.py` file contains a class that implements Logistic Regression from scratch using gradient descent.
- The `main.py` file is used to test the Logistic Regression implementation with the dataset.
- The `Logistic_Regression.pdf` document provides a step-by-step explanation of the mathematical derivation of logistic regression.

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/LogisticRegression.git
   cd LogisticRegression
   ```
2. Install necessary dependencies (if any):
   ```sh
   pip install numpy pandas matplotlib
   ```
3. Run the test script:
   ```sh
   python main.py
   ```

## Credits
- Kaggle Open Dataset: [Diabetes Dataset](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset)
- Logistic Regression by StatQuest: [Logistic Regression Clearly Explained by StatQuest](https://www.youtube.com/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe)
