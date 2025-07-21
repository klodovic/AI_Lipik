
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def quick_eda(path):
    """
    Učitava CSV ili XLSX datoteku, ispisuje info() i head().

    path : str - putanja do CSV ili xlsx datoteke
    """
    if (path.split(".")[-1]) == 'csv':
        df = pd.read_csv(path)
    elif(path.split(".")[-1]) == 'xlsx':
        df = pd.read_xslx(path)
        
    print("="*40)
    print("INFO:")
    print("="*40)
    print(df.info())
    print("\n")
    print("="*40)
    print("DATAFRAME:")
    print("="*40)
    print(df)
    return df


def iqr_method(series):
    """
    Primjenjuje IQR metodu za detekciju outliera i ograničava (cap) ekstremne vrijednosti 
    na granice izračunate iz IQR raspona.

    Args:
        series (pd.Series): Numerička kolona
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Primjena cappinga
    # Sve vrijednosti manje od donje granice postaju donja granica
    # Sve vrijednosti veće od gornje granice postaju gornja granica
    capped_series = series.clip(lower=lower_bound, upper=upper_bound)
    return capped_series


def estimated_work_experience_calculations(df):
    """
    Računa projenjeni radni staž osobe temeljem starosti osobe i njenog stupnja obrazovanja
    

    Args:
        Dataframe
    """
    for row_index, row in df.iterrows():
        if row["Obrazovanje"] == "SSS":
            print(f'Godine radnog staža (SSS): {row["Starost_Klijenta"] - 19}')
        elif row["Obrazovanje"] == "VSS":
            print(f'Godine radnog staža (VSS): {row["Starost_Klijenta"] - 25}')
        elif row["Obrazovanje"] == "Magisterij":
            print(f'Godine radnog staža (Magisterij): {row["Starost_Klijenta"] - 27}')







    