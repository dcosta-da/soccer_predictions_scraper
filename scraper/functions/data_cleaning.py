import pandas as pd
import re
from datetime import datetime
import pytz

def clean_data(match_data):
    df = pd.DataFrame(match_data)

    df['Date'] = df['Date'].apply(format_date)
    
    df[['Country', 'Championship']] = df['Championship'].str.split(n=1, expand=True)
    
    df['Match'] = df['Match'].str.replace('\n—\n', ' - ', regex=False)
    
    return df


def format_date(date_str):
    cleaned_date = date_str.replace('On ', '').split(' GMT')[0].strip()
    cleaned_date = re.sub(r'(th|st|nd|rd)', '', cleaned_date).strip()

    dt_gmt = datetime.strptime(cleaned_date, '%d %B %Y at %H:%M')
    dt_gmt = pytz.timezone('GMT').localize(dt_gmt)

    dt_paris = dt_gmt.astimezone(pytz.timezone('Europe/Paris'))

    return dt_paris 


def process_data(df):
    columns_to_convert = ['Home Win (%)', 'Home Odds', 'Away Win (%)', 'Away Odds',
                          'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5', 'Btts (%)', 'Odds btts']
    for column in columns_to_convert:
        df[column] = df[column].str.replace('%', '').str.strip()
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    return df


def compute_ev(df):
    df['EV home win'] = round(((df['Home Win (%)'] / 100) * ((df['Home Odds'] - 1))) - ((1 - (df['Home Win (%)'] / 100)) * 1), 2)
    df['EV away win'] = round(((df['Away Win (%)'] / 100) * ((df['Away Odds'] - 1))) - ((1 - (df['Away Win (%)'] / 100)) * 1), 2)
    df['EV btts'] = round(((df['Btts (%)'] / 100) * ((df['Odds btts'] - 1))) - ((1 - (df['Btts (%)'] / 100)) * 1), 2)
    df['EV over 2.5'] = round(((df['Over 2.5 (%)'] / 100) * ((df['Odds 2.5'] - 1))) - ((1 - (df['Over 2.5 (%)'] / 100)) * 1), 2)
    
    return df

