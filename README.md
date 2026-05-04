# Diabetes Readmission Prediction Using Structured Health Data

CS 549 Machine Learning, San Diego State University, Spring 2026

Group 20: Niki Liao, Javi Garcia, Adrian Serrano, Jackson Adams

## About

This project predicts whether a diabetic patient will be readmitted to the hospital within 30 days of discharge. We use the Diabetes 130-US Hospitals dataset (1999-2008) from the UCI Machine Learning Repository and compare four classification models: Logistic Regression, Random Forest, K-Nearest Neighbors, and XGBoost.

## Dataset

The dataset comes from the UCI Machine Learning Repository and contains 101,766 inpatient records collected across 130 U.S. hospitals over 10 years. Each record has about 50 features covering patient demographics, admission details, diagnoses (ICD-9 codes), medications, and lab results.

Source: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

Download the dataset and place `diabetic_data.csv` in the `data/` folder before running the notebook.

## Project Structure

```
ml-diabetes-readmission/
    diabetes_readmission.ipynb       main notebook (run this)
    requirements.txt                 python dependencies
    README.md                        this file
    data/
        diabetic_data.csv            dataset (download from UCI)
    reports/
        model_comparison.csv         summary metrics table
        roc_curves.png               ROC curve comparison
        precision_recall_curves.png  PR curve comparison
        confusion_matrices.png       confusion matrices for all models
        feature_importance.png       feature importance comparison
        metrics_comparison.png       bar chart of metrics
        threshold_analysis.png       threshold vs precision/recall/F1
        probability_distributions.png  predicted probability histograms
        calibration_curves.png       calibration curve comparison
        radar_chart.png              radar chart of all metrics
        runtime_comparison.png       training and inference time comparison
        data_overview.png            class distribution and missing values
        smote_comparison.png         before/after SMOTE balancing
```

## Environment

This project was developed and tested with:

    Python 3.10+
    OS: macOS Sequoia 15.4 (Apple M4)
    IDE: Visual Studio Code with Jupyter extension

All required packages are listed in requirements.txt.

## How to Run

1. Clone or download the repository:

```
git clone https://github.com/your-repo/ml-diabetes-readmission.git
cd ml-diabetes-readmission
```

2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

```
source venv/bin/activate       # mac/linux
venv\Scripts\activate          # windows
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Download the dataset from the UCI link above and place `diabetic_data.csv` inside the `data/` folder.

6. Open the notebook in VS Code or Jupyter:

```
# option 1: VS Code (recommended)
code diabetes_readmission.ipynb

# option 2: Jupyter
jupyter notebook diabetes_readmission.ipynb
```

7. Make sure the kernel is set to the venv you created (in VS Code, click the kernel picker in the top right of the notebook and select the venv Python interpreter).

8. Run all cells from top to bottom. The notebook handles everything: data loading, preprocessing, model training, evaluation, and generating all comparison plots in the `reports/` folder.

Note: The full run takes about 20-30 minutes depending on your hardware because of the cross-validation and hyperparameter tuning. KNN and XGBoost take the longest.

## Models

Each team member implemented one model:

    Niki: Random Forest (bagging ensemble)
    Javi: K-Nearest Neighbors (instance-based classifier)
    Adrian: Logistic Regression (baseline, linear classifier)
    Jackson: XGBoost (sequential boosting ensemble)

All models are tuned using cross-validation (GridSearchCV or RandomizedSearchCV) with F1 score as the optimization target. We also use threshold optimization to find the best decision boundary for each model since the default 0.5 threshold performs poorly on imbalanced data.

## Evaluation Metrics

We evaluate each model using accuracy, precision, recall, F1 score, ROC AUC, confusion matrices, calibration curves, threshold analysis, probability distributions, and runtime analysis. Recall is our most important metric because missing a high-risk patient (false negative) is more costly than a false alarm in clinical settings.
