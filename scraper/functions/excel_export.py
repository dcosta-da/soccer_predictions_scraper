import os
import pandas as pd

def export_to_excel(df):
    base_dir = os.path.dirname(os.path.dirname(__file__)) 
    data_dir = os.path.join(base_dir, "data") 
    os.makedirs(data_dir, exist_ok=True)  

    file_path = os.path.join(data_dir, "betclever_predictions.xlsx")

    sheets = {
    "Home win": df[(df['Home Win (%)'] >= 70) & (df['Home Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Home Win (%)', 'Home Odds']],
    "Away Win": df[(df['Away Win (%)'] >= 70) & (df['Away Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Away Win (%)', 'Away Odds']],
    "Draw": df[df['Draw (%)'] >= 60][['Date', 'Country', 'Championship', 'Match', 'Draw (%)', 'Draw Odds']],
    "Btts": df[(df['Btts (%)'] >= 75) & (df['Odds btts'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Btts (%)', 'Odds btts']],
    "Over_Under": df[
        ((df['Over 2.5 (%)'] >= 80) & (df['Odds 2.5'] >= 1.7)) |
        ((df['Over 3.5 (%)'] >= 60) & (df['Odds 3.5'] >= 2.2))
    ][['Date', 'Country', 'Championship', 'Match', 'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5']]
    }
    
    # Si le fichier existe déjà, on l'ouvre en mode ajout
    if os.path.exists(file_path):
        with pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
            for sheet_name, df_filtered in sheets.items():
                if not df_filtered.empty:
                    df_filtered.to_excel(writer, index=False, sheet_name=sheet_name)
    else:
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            for sheet_name, df_filtered in sheets.items():
                if not df_filtered.empty:
                    df_filtered.to_excel(writer, index=False, sheet_name=sheet_name)
    
    print(f"Les données ont été enregistrées ou mises à jour dans {file_path}")
