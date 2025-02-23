# Linear Regression from Scratch

## Overview
This project implements Linear Regression from scratch using Python. The goal is to understand and implement the core mathematical concepts behind linear regression without relying on high-level libraries like Scikit-Learn.

## Folder Structure
```
LinearRegression/
│── Linear Regression Concept Notes (Mathematical Derivation)
│── LinearRegression.py  (Implementation of the Linear Regression class)
│── data.csv  (Dataset used for testing, sourced from Kaggle)
│── main.py  (Testing and running the Linear Regression model)
```

## Dataset
The dataset used (`data.csv`) is sourced from Kaggle Open Datasets:
[House Price Prediction Dataset](https://www.kaggle.com/datasets/shree1992/housedata)

## Mathematical Foundation
The theoretical derivation of Linear Regression used in this project is based on the following references:
- [Lecture Notes on Multiple Regression (CMU)](https://www.stat.cmu.edu/~cshalizi/mreg/15/lectures/13/lecture-13.pdf)
- [Linear and Quadratic Gradients (UBC)](https://www.cs.ubc.ca/~schmidtm/Courses/340-F16/linearQuadraticGradients.pdf)

## Implementation Details
- The `LinearRegression.py` file contains a class that implements Linear Regression from scratch using gradient descent.
- The `main.py` file is used to test the Linear Regression implementation with the dataset.
- The `Linear Regression Concept Notes` document provides a step-by-step explanation of the mathematical derivation of linear regression.

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/LinearRegression.git
   cd LinearRegression
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
- Kaggle Open Dataset: [House Price Prediction Dataset](https://www.kaggle.com/datasets/shree1992/housedata)
- CMU Lecture Notes: [Lecture-13](https://www.stat.cmu.edu/~cshalizi/mreg/15/lectures/13/lecture-13.pdf)
- UBC Notes: [Linear and Quadratic Gradients](https://www.cs.ubc.ca/~schmidtm/Courses/340-F16/linearQuadraticGradients.pdf)
