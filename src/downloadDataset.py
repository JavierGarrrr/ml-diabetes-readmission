import os
import pandas as pd


DATA_PATH = "data/raw.csv"


def download_data():
    #Download the diabetes dataset from UCI and save to CSV.
    os.makedirs("data", exist_ok=True) # make sure the data directory exists

    # try to download using ucimlrepo
    try:
        from ucimlrepo import fetch_ucirepo
        print("Downloading via ucimlrepo...")
        dataset = fetch_ucirepo(id=296) # get the diabetes dataset
        df = dataset.data.original # get the original data as a DataFrame
    except ImportError:
        # uci didn't work, try with direct download
        print("ucimlrepo not found, falling back to direct download...")
        url = (
            "https://archive.ics.uci.edu/static/public/296/"
            "dataset.csv"  # direct CSV link
        )
        df = pd.read_csv(url)

    # save to local CSV
    df.to_csv(DATA_PATH, index=False)
    print(f"Saved {df.shape[0]} rows x {df.shape[1]} columns to '{DATA_PATH}'")
    return df


def load_data(path=DATA_PATH):
    #Load the dataset from a local CSV file.
    df = pd.read_csv(path)
    print(f"Loaded: {df.shape[0]} rows x {df.shape[1]} columns")
    print(df.head())
    return df



if __name__ == "__main__":
    if os.path.exists(DATA_PATH) and os.path.getsize(DATA_PATH) > 0:
        print("File already exists - loading from disk.")
        df = load_data()
    else:
        print("File not found or empty - downloading...")
        df = download_data()
        load_data()