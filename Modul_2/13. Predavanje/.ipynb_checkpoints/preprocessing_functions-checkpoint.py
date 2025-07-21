# preprocessing_functions.py
import pandas as pd
import numpy as np

def clean_categorical_title(df, column_name):
    """
    Primjenjuje .str.title() na specificiranu kolonu u DataFrameu.
    """
    if column_name not in df.columns:
        print(f"Upozorenje: Kolona '{column_name}' ne postoji u DataFrameu.")
        return df
    df[column_name] = df[column_name].str.title()
    return df

# Ovdje možete dodati i druge funkcije

def mode_insert(df, column_name):
    """
    Primjenjuje najčešću vrijednost u koloni i unosi ih u prazne čelije.
    Funkcija prima dataframe i naziv kolone.
    """
    if column_name not in df.columns:
        print(f"Upozorenje: Kolona '{column_name}' ne postoji u DataFrameu.")
        return df
    mode_value = df[column_name].mode()
    df[column_name].fillna(value = mode_value, inplace = True)
    return df