import pandas as pd
import numpy as np

PATH = "data/diabetic_data.csv"
MISSING_SYMBOL = "?"

def load(path):
    df = pd.read_csv(path)
    print(f"Loaded: {df.shape[0]} rows x {df.shape[1]}")
    print(df.head())
    return df

def audit_missing(df):
    records = []
    for col in df.columns:
        num_nan = df[col].isna().sum()
        num_sym = (df[col] == MISSING_SYMBOL).sum()
        num_missing = num_nan + num_sym
        percent_missing = num_missing / len(df[col]) * 100
        records.append({
            "column"    : col,
            "nan"       : num_nan,
            "?"         : num_sym,
            "total_missing"   : num_missing,
            "%_missing" : percent_missing
        })
    report = pd.DataFrame(records)
    report.query("total_missing > 1")
    report.sort_values("%_missing", ascending=False)
    report.reset_index(drop=True)
    return report

def remove_main(df):
    df = df.copy()
    cols_dropped = ["weight", "max_glu_serum", "A1Cresult", "payer_code", "medical_specialty"]
    df = df.drop(columns=cols_dropped)
    return df





