import pandas as pd
import re

def clean_data(match_data):
    df = pd.DataFrame(match_data)

    df[['Country', 'Championship']] = df['Championship'].str.split(n=1, expand=True)
    df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)

    df['Date'] = df['Date'].apply(format_date)
    
    return df

def format_date(date_str):
    cleaned_date = date_str.replace('On ', '').split(' GMT')[0].strip()
    cleaned_date = re.sub(r'(th|st|nd|rd)', '', cleaned_date).strip()
    return pd.to_datetime(cleaned_date, format='%d %B %Y at %H:%M').strftime('%d-%m-%Y %H:%M')

def process_data(df):
    # Nettoyer et convertir les colonnes numériques
    columns_to_convert = ['Home Win (%)', 'Home Odds', 'Draw (%)', 'Draw Odds', 'Away Win (%)', 'Away Odds', 'Over 1.5 (%)', 'Odds 1.5', 'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5', 'Btts (%)', 'Odds btts']
    for column in columns_to_convert:
        df[column] = df[column].str.replace('%', '').str.strip()
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df
