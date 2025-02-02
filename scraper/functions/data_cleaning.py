import pandas as pd
import re
from datetime import datetime
import pytz

def clean_data(match_data):
    df = pd.DataFrame(match_data)

    # Nettoyer les données comme dans ton code original
    df['Date'] = df['Date'].apply(format_date)
    
    # Diviser la colonne 'Championship' en 'Country' et 'Championship'
    df[['Country', 'Championship']] = df['Championship'].str.split(n=1, expand=True)
    
    # Remplacer '\n—\n' dans la colonne 'Match'
    df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)
    
    return df


def format_date(date_str):
    cleaned_date = date_str.replace('On ', '').split(' GMT')[0].strip()
    cleaned_date = re.sub(r'(th|st|nd|rd)', '', cleaned_date).strip()

    dt_gmt = datetime.strptime(cleaned_date, '%d %B %Y at %H:%M')
    dt_gmt = pytz.timezone('GMT').localize(dt_gmt)

    dt_paris = dt_gmt.astimezone(pytz.timezone('Europe/Paris'))

    return dt_paris.strftime('%d-%m-%Y %H:%M')


def process_data(df):
    # Nettoyer et convertir les colonnes numériques
    columns_to_convert = ['Home Win (%)', 'Home Odds', 'Draw (%)', 'Draw Odds', 'Away Win (%)', 'Away Odds', 'Over 1.5 (%)', 'Odds 1.5', 'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5', 'Btts (%)', 'Odds btts']
    for column in columns_to_convert:
        df[column] = df[column].str.replace('%', '').str.strip()
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df
