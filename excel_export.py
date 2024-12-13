import os
import pandas as pd

def export_to_excel(df):
    file_path = "betclever_predictions.xlsx"
    sheets = {
        "Home win": df[(df['Home Win (%)'] >= 70) & (df['Home Odds'] >= 1.7)],
        # Ajouter d'autres filtres pour chaque feuille de ton Excel
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
