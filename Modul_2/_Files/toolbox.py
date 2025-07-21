import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def quick_eda(path):
    """
    Učitava CSV datoteku, ispisuje info() i head().

    path : str - putanja do CSV datoteke
    """
    ext = path.split(".")[-1]
    if ()
    df = pd.read_csv(path)
    print("="*40)
    print("INFO:")
    print("="*40)
    print(df.info())
    print("\n")
    print("="*40)
    print(f"DATAFRAME")
    print("="*40)
    print(df)
    return df
