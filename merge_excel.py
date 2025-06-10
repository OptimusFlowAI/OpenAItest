import pandas as pd
import glob

# Alle Excel-Dateien im aktuellen Ordner suchen
excel_files = glob.glob("*.xlsx")

# Liste zum Sammeln der DataFrames
dfs = []

for file in excel_files:
    df = pd.read_excel(file)
    
    # Spalten vereinheitlichen (z. B. "E-Mail" und "Email" angleichen)
    df.columns = df.columns.str.strip().str.lower().str.replace("e-mail", "email")
    
    dfs.append(df)

# Alles zusammenführen
merged_df = pd.concat(dfs, ignore_index=True)

# Duplikate anhand einer bestimmten Spalte entfernen (z. B. „email“)
merged_df = merged_df.drop_duplicates(subset="email")

# Ergebnis speichern
merged_df.to_excel("merged_result.xlsx", index=False)

