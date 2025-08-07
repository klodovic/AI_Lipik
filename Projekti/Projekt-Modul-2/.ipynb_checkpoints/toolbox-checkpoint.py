import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# 1. Kreiranje dataframe-a iz csv ili excel datoteke
# ---------------------------------------------------
def quick_eda(path):
    """
    Učitava CSV ili XLSX datoteku, ispisuje info() i head().

    Args:
        path (str): putanja do CSV ili XLSX datoteke

    Returns:
        pd.DataFrame: učitani DataFrame
    """
    ext = path.split(".")[-1].lower()
    if ext == 'csv':
        df = pd.read_csv(path)
    elif ext == 'xlsx':
        df = pd.read_excel(path)
    else:
        raise ValueError("Nepodržani format datoteke. Podržani su samo CSV i XLSX.")

    print("="*40)
    print("INFO:")
    print("="*40)
    print(df.info())
    print("\n")
    print("="*40)
    print("DATAFRAME (prvih 5 redaka):")
    print("="*40)
    print(df.head())
    return df

# -----------------------------------------------
# 2. Groupby s podrškom za agregacijske funkcije
# -----------------------------------------------
def df_groupby(df, variables, agg_func=None):
    """
    Grupira podatke u DataFrameu po zadanim varijablama i primjenjuje agregacijsku funkciju.

    Args:
        df (pd.DataFrame): Ulazni DataFrame.
        variables (str ili list): Naziv jednog stupca ili lista naziva stupaca po kojima se grupira.
        agg_func (str, opcionalno): Naziv agregacijske funkcije koju treba primijeniti.
            Podržane vrijednosti: "sum", "mean", "median", "min", "max", "std", "count", "size".
            Ako je None, vraća se groupby objekt bez agregacije.

    Returns:
        pd.DataFrame ili pd.core.groupby.DataFrameGroupBy: Grupirani i agregirani podaci ili groupby objekt.
    """
    if isinstance(variables, str):
        variables = [variables]

    grouped = df.groupby(variables)

    if agg_func == "sum":
        return grouped.sum()
    elif agg_func == "mean":
        return grouped.mean()
    elif agg_func == "median":
        return grouped.median()
    elif agg_func == "min":
        return grouped.min()
    elif agg_func == "max":
        return grouped.max()
    elif agg_func == "std":
        return grouped.std()
    elif agg_func == "size":
        return grouped.size().reset_index(name='Count')
    elif agg_func == "count":
        return grouped.count()
    elif agg_func is None:
        return grouped
    else:
        raise ValueError(f"Nepoznata agregacijska funkcija: {agg_func}")

# -----------------------------------------------
# 3. Groupby s više agregacijskih funkcija za jedan stupac
# -----------------------------------------------
def agg_column_multi(df, group_vars, column, agg_funcs):
    """
    Grupira DataFrame po zadanim varijablama i primjenjuje više agregacijskih funkcija na jedan stupac.

    Args:
        df (pd.DataFrame): originalni DataFrame
        group_vars (str ili list): varijabla ili lista varijabli po kojima se grupira
        column (str): stupac za agregaciju
        agg_funcs (list): lista funkcija (npr. ["mean", "min", "max"])

    Returns:
        pd.DataFrame: Agregirani rezultati
    """
    if isinstance(group_vars, str):
        group_vars = [group_vars]
    grouped = df.groupby(group_vars)
    return grouped[column].agg(agg_funcs)

# -------------------------------------
# 4. Pie chart za grupirane vrijednosti
# -------------------------------------
def plot_pie(df, group_col, value_col):
    """
    Crta pie chart na temelju srednje vrijednosti value_col unutar group_col.

    Args:
        df (pd.DataFrame): DataFrame s podacima
        group_col (str): kategorijska kolona po kojoj se grupira
        value_col (str): numerička kolona čije se srednje vrijednosti prikazuju
    """
    df.groupby(group_col)[value_col].mean().plot(kind='pie', autopct='%.2f', figsize=(6, 6))
    plt.title(f"Prosječna vrijednost '{value_col}' po '{group_col}'")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# -------------------------------------
# 5. Histogram s KDE za numeričku kolonu
# -------------------------------------
def plot_histogram(df, column, bins=50, kde=True):
    """
    Crta histogram s opcionalnom KDE krivuljom.

    Args:
        df (pd.DataFrame): DataFrame
        column (str): Naziv numeričke kolone
        bins (int): Broj binova (default 50)
        kde (bool): Prikaz KDE krivulje (default True)
    """
    sns.histplot(df[column], bins=bins, kde=kde)
    plt.title(f"Distribucija - {column}")
    plt.xlabel(column)
    plt.ylabel("Frekvencija")
    plt.show()

# -------------------------------------
# 6. Boxplot za jednu numeričku varijablu
# -------------------------------------
def plot_boxplot(df, column):
    """
    Crta boxplot za zadanu numeričku kolonu.

    Args:
        df (pd.DataFrame): DataFrame
        column (str): Naziv kolone
    """
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot - {column}")
    plt.xlabel(column)
    plt.show()

# -------------------------------------
# 7. Korelacijska matrica (heatmap)
# -------------------------------------
def plot_correlation_matrix(df):
    """
    Crta korelacijsku matricu za sve numeričke kolone.

    Args:
        df (pd.DataFrame): DataFrame
    """
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Korelacija numeričkih varijabli")
    plt.show()


# -------------------------------------
# 8. Bar chart po grupi
# -------------------------------------
def plot_bar(df, group_var, value_var, agg_func="mean", title=None, xlabel=None, ylabel=None):
    """
    Crta bar chart na temelju grupirane varijable i agregirane vrijednosti.

    Args:
        df (pd.DataFrame): DataFrame za analizu
        group_var (str): Stupac po kojem se grupira
        value_var (str): Stupac čije se vrijednosti agregiraju
        agg_func (str): Agregacijska funkcija (npr. "mean", "sum", "count")
        title (str): Naslov grafa
        xlabel (str): Oznaka x-osi
        ylabel (str): Oznaka y-osi
    """
    grouped = df.groupby(group_var)[value_var].agg(agg_func)
    grouped.plot(kind='bar')
    plt.title(title or f"{agg_func.capitalize()} {value_var} po {group_var}")
    plt.xlabel(xlabel or group_var)
    plt.ylabel(ylabel or f"{agg_func.capitalize()} {value_var}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -------------------------------------
# 9. Scatterplot između dvije numeričke varijable
# -------------------------------------
def plot_scatter(df, x_var, y_var, hue=None, title=None):
    """
    Crta scatterplot (raspršeni graf) između dviju varijabli.

    Args:
        df (pd.DataFrame): DataFrame s podacima
        x_var (str): Varijabla za x-os
        y_var (str): Varijabla za y-os
        hue (str): (Opcionalno) Kategorijska varijabla za boje
        title (str): Naslov grafa
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_var, y=y_var, hue=hue)
    plt.title(title or f"{y_var} vs {x_var}")
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.tight_layout()
    plt.show()

# -------------------------------------
# 10. Broj ponavljanja po kategoriji
# -------------------------------------
def plot_count(df, column, hue=None, title=None):
    """
    Prikazuje countplot za zadanu kategorijsku varijablu.

    Args:
        df (pd.DataFrame): DataFrame s podacima
        column (str): Naziv varijable za os X
        hue (str, optional): Varijabla za boju (npr. target klasa)
        title (str, optional): Naslov grafa
    """
    sns.countplot(data=df, x=column, hue=hue)
    plt.title(title or f"Distribucija vrijednosti - {column}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -------------------------------------
# 11. Parni odnosi između numeričkih varijabli
# -------------------------------------
def plot_pairplot(df, hue=None):
    """
    Prikazuje parne odnose između numeričkih varijabli (pairplot).

    Args:
        df (pd.DataFrame): DataFrame s numeričkim podacima
        hue (str, optional): Kategorijska varijabla za boju
    """
    sns.pairplot(df, hue=hue, corner=True)
    plt.show()

# ------------------------------------
# 12. IQR metodu za detekciju outliera
# ------------------------------------
def iqr_method(series):
    """
    Primjenjuje IQR metodu za detekciju outliera i ograničava (cap) ekstremne vrijednosti.

    Args:
        series (pd.Series): Numerička kolona

    Returns:
        pd.Series: Ograničena serija bez outliera (capped)
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series.clip(lower=lower_bound, upper=upper_bound)





############### CUSTOM #############################
# ------------------------------------
# 1. Procjena radnog staža na temelju obrazovanja i starosti
# ------------------------------------
def estimated_work_experience_calculations(df):
    """
    Računa procijenjeni radni staž osobe temeljem starosti i stupnja obrazovanja.

    Args:
        df (pd.DataFrame): DataFrame koji sadrži stupce 'Starost_Klijenta' i 'Obrazovanje'
    """
    for _, row in df.iterrows():
        if row["Obrazovanje"] == "SSS":
            print(f'Godine radnog staža (SSS): {row["Starost_Klijenta"] - 19}')
        elif row["Obrazovanje"] == "VSS":
            print(f'Godine radnog staža (VSS): {row["Starost_Klijenta"] - 25}')
        elif row["Obrazovanje"] == "Magisterij":
            print(f'Godine radnog staža (Magisterij): {row["Starost_Klijenta"] - 27}')

# Opcionalno možeš definirati što se iz ovog modula može direktno importirati
__all__ = [
    "quick_eda",
    "df_groupby",
    "agg_column_multi",
    "iqr_method",
    "estimated_work_experience_calculations",
    "plot_pie",
    "plot_histogram",
    "plot_boxplot",
    "plot_correlation_matrix",
    "plot_bar",
    "plot_scatter"
] 