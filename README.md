# Diabetes Readmission Prediction Using Structured Health Data

CS 549 Machine Learning, San Diego State University, Spring 2026

Group 20: Niki Liao, Javi Garcia, Adrian Serrano, Jackson Adams

## About

In this project, we will prediciting if a diabetic patient will need to be readmitted to the hospital within 30 days after beign discharge.  We use a dataset from the UCI Machine Learning Repository and compare four classification models which includes logistic regression, random forest, K-nearest neighbors and XGBoost.

## Dataset

The dataset as mentioned abobe is from the UCI Machine Learning Repository and has around 100,000 inpatient records collected across 130 U.S. hospitals over 10 years. Here is the link to the dataset: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

## Environment

For this project we used:

    Python 3.10+
    For OS we used MacOS
    For IDE we used Visual Studio Code with jupyter extension

In additoin to that all the required packages are listed in requirements.txt

## How to Run

1. Open the project file on your IDE

2. Go to the terminal and create a virtual environment

```
python3 -m venv venv
```

3. Activate the virtual environment

```
source venv/bin/activate  
```

4. Install all the dependencies

```
pip install -r requirements.txt
```

5. Run the .pynb file and make sure the kernel is set to the venv you created

   On VS Code click the kernel picker in the top right of the notebook and select the venv Python interpreter

6. Click Run All and all the plots and tables will be generated on the report folder. 

   Note: The full run takes about 20-30 minutes depending on your hardware because of the cross-validation and hyperparameter tuning. KNN and XGBoost take the longest

## Models

Each of us implemented one model:

    Niki: Random Forest
    Javi: K-Nearest Neighbors
    Adrian: Logistic Regression 
    Jackson: XGBoos

