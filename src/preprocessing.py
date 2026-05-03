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
    report = (
        pd.DataFrame(records)
        .query("total_missing > 0")
        .sort_values("%_missing", ascending=False)
        .reset_index(drop=True)
    )
    return report

def remove_main(df):
    df = df.copy()
    cols_dropped = ["weight", "max_glu_serum", "A1Cresult", "payer_code"]
    df = df.drop(columns=cols_dropped)
    return df

def replace_missing(df):
    df = df.copy()
    df = df.replace(MISSING_SYMBOL, np.nan)
    return df

def fill_mode(df, col_name):
    df = df.copy()
    mode_val = df[col_name].mode()[0]
    df[col_name] = df[col_name].fillna(mode_val)
    return df

def fill_unknown(df, col_name):
    df = df.copy()
    df[col_name] = df[col_name].fillna("Unknown")
    return df

def remove_duplicates(df):
    df = df.sort_values("encounter_id")
    df = df.drop_duplicates("patient_nb", keep = "first")
    return df

def remove_discharge_records(df):
    removal_ids = [11,13,14,19,20,21]
    mask = df["discharge_disposition_id"].isin(removal_ids)
    df = df[~mask]
    return df

def testing(PATH, MISSING_SYMBOL):
    print("--------------------------")
    print("init")
    print("--------------------------")
    df = load(PATH)
    report = audit_missing(df)
    print("--------------------------")
    print("Report initial results")
    print("--------------------------")
    print(report)
    df = remove_main(df)
    df = replace_missing(df)
    df = fill_mode(df, "race")
    df = fill_mode(df, "diag_1")
    df = fill_mode(df, "diag_2")
    df = fill_mode(df, "diag_3")
    df = remove_discharge_records(df)
    df = fill_unknown(df, "medical_specialty")
    report2 = audit_missing(df)
    print("--------------------------")
    print("Report new results after removal")
    print("--------------------------")
    print(report2)
    return df


df = testing(PATH, MISSING_SYMBOL)










