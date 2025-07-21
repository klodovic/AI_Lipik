import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def quick_eda(path):
    """
    Učitava CSV datoteku, ispisuje info(), head() i describe().

    path : str - putanja do CSV datoteke
    head_rows : int - koliko redova prikazati
    """
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
