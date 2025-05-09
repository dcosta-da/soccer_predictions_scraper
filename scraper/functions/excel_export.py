import os
import pandas as pd

# def export_to_excel(df):
#     base_dir = os.path.dirname(os.path.dirname(__file__)) 
#     data_dir = os.path.join(base_dir, "data") 
#     os.makedirs(data_dir, exist_ok=True)  

#     file_path = os.path.join(data_dir, "betclever_predictions.xlsx")

#     sheets = {
#     "Home win": df[(df['Home Win (%)'] >= 70) & (df['Home Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Home Win (%)', 'Home Odds']],
#     "Away win": df[(df['Away Win (%)'] >= 70) & (df['Away Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Away Win (%)', 'Away Odds']],
#     "Btts": df[(df['Btts (%)'] >= 75) & (df['Odds btts'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Btts (%)', 'Odds btts']],
#     "Over_Under": df[
#         ((df['Over 2.5 (%)'] >= 80) & (df['Odds 2.5'] >= 1.7)) |
#         ((df['Over 3.5 (%)'] >= 60) & (df['Odds 3.5'] >= 2.2))][['Date', 'Country', 'Championship', 'Match', 'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5']],
#     "EV Home win" : df[(df['Home Win (%)'] >= 50) & (df['Home Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Home Win (%)', 'Home Odds', 'EV home win']],
#     "EV Away win" : df[(df['Away Win (%)'] >= 50) & (df['Away Odds'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Away Win (%)', 'Away Odds', 'EV away win']],
#     "EV Over 2.5" : df[(df['Over 2.5 (%)'] >= 70) & (df['Odds 2.5'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Over 2.5 (%)', 'Odds 2.5', 'EV over 2.5']],
#     "EV Btts" : df[(df['Btts (%)'] >= 65) & (df['Odds btts'] >= 1.7)][['Date', 'Country', 'Championship', 'Match', 'Btts (%)', 'Odds btts', 'EV btts']],
#     }
    
#     if os.path.exists(file_path):
#         with pd.ExcelWriter(file_path, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
#             for sheet_name, df_filtered in sheets.items():
#                 if not df_filtered.empty:
#                     df_filtered.to_excel(writer, index=False, sheet_name=sheet_name)
#     else:
#         with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
#             for sheet_name, df_filtered in sheets.items():
#                 if not df_filtered.empty:
#                     df_filtered.to_excel(writer, index=False, sheet_name=sheet_name)
    
#     print(f"Les données ont été enregistrées ou mises à jour dans {file_path}")

def export_to_excel(df):
    import os
    import pandas as pd

    base_dir = os.path.dirname(os.path.dirname(__file__)) 
    data_dir = os.path.join(base_dir, "data") 
    os.makedirs(data_dir, exist_ok=True)  
    file_path = os.path.join(data_dir, "betclever_predictions.xlsx")

    # Création colonne "Match" si absente
    if "Match" not in df.columns:
        print("La colonne 'Match' est absente des données, création avec NaN.")
        df["Match"] = pd.NA

    def filter_df(required_cols, condition_func, selected_cols, label="inconnue"):
        missing = [col for col in required_cols if col not in df.columns]
        if missing:
            print(f"Colonnes manquantes pour '{label}': {', '.join(missing)}. Remplissage avec NaN.")
            return pd.DataFrame(columns=selected_cols)
        try:
            filtered_df = df[condition_func(df)][selected_cols]
            return filtered_df
        except Exception as e:
            print(f"Erreur lors du filtrage '{label}': {e}")
            return pd.DataFrame(columns=selected_cols)

    sheets = {
        "Home win": filter_df(
            ['Home Win (%)', 'Home Odds'], 
            lambda df: (df['Home Win (%)'] >= 70) & (df['Home Odds'] >= 1.7), 
            ['Date', 'Country', 'Championship', 'Match', 'Home Win (%)', 'Home Odds'],
            "home win"
        ),
        "Away win": filter_df(
            ['Away Win (%)', 'Away Odds'],
            lambda df: (df['Away Win (%)'] >= 70) & (df['Away Odds'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Away Win (%)', 'Away Odds'],
            "away win"
        ),
        "Btts": filter_df(
            ['Btts (%)', 'Odds btts'],
            lambda df: (df['Btts (%)'] >= 75) & (df['Odds btts'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Btts (%)', 'Odds btts'],
            "btts"
        ),
        "Over_Under": filter_df(
            ['Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5'],
            lambda df: ((df['Over 2.5 (%)'] >= 80) & (df['Odds 2.5'] >= 1.7)) | ((df['Over 3.5 (%)'] >= 60) & (df['Odds 3.5'] >= 2.2)),
            ['Date', 'Country', 'Championship', 'Match', 'Over 2.5 (%)', 'Odds 2.5', 'Over 3.5 (%)', 'Odds 3.5'],
            "over_under"
        ),
        "EV Home win": filter_df(
            ['Home Win (%)', 'Home Odds', 'EV home win'],
            lambda df: (df['Home Win (%)'] >= 50) & (df['Home Odds'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Home Win (%)', 'Home Odds', 'EV home win'],
            "EV home win"
        ),
        "EV Away win": filter_df(
            ['Away Win (%)', 'Away Odds', 'EV away win'],
            lambda df: (df['Away Win (%)'] >= 50) & (df['Away Odds'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Away Win (%)', 'Away Odds', 'EV away win'],
            "EV away win"
        ),
        "EV Over 2.5": filter_df(
            ['Over 2.5 (%)', 'Odds 2.5', 'EV over 2.5'],
            lambda df: (df['Over 2.5 (%)'] >= 70) & (df['Odds 2.5'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Over 2.5 (%)', 'Odds 2.5', 'EV over 2.5'],
            "EV over 2.5"
        ),
        "EV Btts": filter_df(
            ['Btts (%)', 'Odds btts', 'EV btts'],
            lambda df: (df['Btts (%)'] >= 65) & (df['Odds btts'] >= 1.7),
            ['Date', 'Country', 'Championship', 'Match', 'Btts (%)', 'Odds btts', 'EV btts'],
            "EV btts"
        ),
    }

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

