import pandas as pd
import re
from datetime import datetime
import pytz
import numpy as np

# def clean_data(match_data):
#     df = pd.DataFrame(match_data)

#     df['Date'] = df['Date'].apply(format_date)
    
#     df[['Country', 'Championship']] = df['Championship'].str.split(n=1, expand=True)
    
#     df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)
    
#     return df

# def clean_data(match_data):
#     df = pd.DataFrame(match_data)

#     # Vérification si la colonne 'Date' existe
#     if 'Date' in df.columns:
#         df['Date'] = df['Date'].apply(format_date)
#     else:
#         print("La colonne 'Date' est absente des données, remplacement par NaN.")
#         # Remplacer les valeurs manquantes par NaN
#         df['Date'] = np.nan

#     df[['Country', 'Championship']] = df['Championship'].str.split(n=1, expand=True)
    
#     df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)
    
#     return df

def clean_data(match_data):
    df = pd.DataFrame(match_data)

    # Formatage de la date
    if 'Date' in df.columns:
        df['Date'] = df['Date'].apply(format_date)
    else:
        print("La colonne 'Date' est absente des données, remplacement par NaN.")
        df['Date'] = np.nan

    # Séparation Country / Championship si la colonne existe
    if 'Championship' in df.columns:
        split_cols = df['Championship'].str.split(n=1, expand=True)
        df['Country'] = split_cols[0]
        df['Championship'] = split_cols[1]
    else:
        print("La colonne 'Championship' est absente des données, remplacement par NaN pour 'Country' et 'Championship'.")
        df['Country'] = np.nan
        df['Championship'] = np.nan

    # Nettoyage du champ Match
    if 'Match' in df.columns:
        df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)
    else:
        print("La colonne 'Match' est absente des données, création avec NaN.")
        df['Match'] = np.nan

    return df


def format_date(date_str):
    cleaned_date = date_str.replace('On ', '').split(' GMT')[0].strip()
    cleaned_date = re.sub(r'(th|st|nd|rd)', '', cleaned_date).strip()

    dt_gmt = datetime.strptime(cleaned_date, '%d %B %Y at %H:%M')
    dt_gmt = pytz.timezone('GMT').localize(dt_gmt)

    dt_paris = dt_gmt.astimezone(pytz.timezone('Europe/Paris'))

    return dt_paris.strftime('%d-%m-%Y %H:%M')


# def process_data(df):
#     columns_to_convert = ['Home Win (%)', 'Home Odds', 'Away Win (%)', 'Away Odds',
#                           'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5', 'Btts (%)', 'Odds btts']
#     for column in columns_to_convert:
#         df[column] = df[column].str.replace('%', '').str.strip()
#         df[column] = pd.to_numeric(df[column], errors='coerce')
    
#     return df


def process_data(df):
    columns_to_convert = ['Home Win (%)', 'Home Odds', 'Away Win (%)', 'Away Odds',
                          'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5', 'Btts (%)', 'Odds btts']
    
    for column in columns_to_convert:
        if column in df.columns:
            df[column] = df[column].astype(str).str.replace('%', '').str.strip()
            df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df


# def compute_ev(df):
#     df['EV home win'] = round(((df['Home Win (%)'] / 100) * ((df['Home Odds'] - 1))) - ((1 - (df['Home Win (%)'] / 100)) * 1), 2)
#     df['EV away win'] = round(((df['Away Win (%)'] / 100) * ((df['Away Odds'] - 1))) - ((1 - (df['Away Win (%)'] / 100)) * 1), 2)
#     df['EV btts'] = round(((df['Btts (%)'] / 100) * ((df['Odds btts'] - 1))) - ((1 - (df['Btts (%)'] / 100)) * 1), 2)
#     df['EV over 2.5'] = round(((df['Over 2.5 (%)'] / 100) * ((df['Odds 2.5'] - 1))) - ((1 - (df['Over 2.5 (%)'] / 100)) * 1), 2)
    
#     return df

# def compute_ev(df):
#     if 'Home Win (%)' in df.columns and 'Home Odds' in df.columns:
#         df['EV home win'] = round(((df['Home Win (%)'] / 100) * ((df['Home Odds'] - 1))) - ((1 - (df['Home Win (%)'] / 100)) * 1), 2)

#     if 'Away Win (%)' in df.columns and 'Away Odds' in df.columns:
#         df['EV away win'] = round(((df['Away Win (%)'] / 100) * ((df['Away Odds'] - 1))) - ((1 - (df['Away Win (%)'] / 100)) * 1), 2)

#     if 'Btts (%)' in df.columns and 'Odds btts' in df.columns:
#         df['EV btts'] = round(((df['Btts (%)'] / 100) * ((df['Odds btts'] - 1))) - ((1 - (df['Btts (%)'] / 100)) * 1), 2)

#     if 'Over 2.5 (%)' in df.columns and 'Odds 2.5' in df.columns:
#         df['EV over 2.5'] = round(((df['Over 2.5 (%)'] / 100) * ((df['Odds 2.5'] - 1))) - ((1 - (df['Over 2.5 (%)'] / 100)) * 1), 2)

#     return df

def compute_ev(df):
    ev_calculations = {
        'EV home win': ('Home Win (%)', 'Home Odds'),
        'EV away win': ('Away Win (%)', 'Away Odds'),
        'EV btts': ('Btts (%)', 'Odds btts'),
        'EV over 2.5': ('Over 2.5 (%)', 'Odds 2.5')
    }

    for ev_name, (prob_col, odds_col) in ev_calculations.items():
        if prob_col in df.columns and odds_col in df.columns:
            df[ev_name] = round(
                ((df[prob_col] / 100) * (df[odds_col] - 1)) -
                ((1 - (df[prob_col] / 100)) * 1), 2
            )
        else:
            print(f"Colonnes manquantes pour '{ev_name}': '{prob_col}' ou '{odds_col}'. Remplissage avec NaN.")
            df[ev_name] = np.nan

    return df
