import pandas as pd
import os

# === Set working directory to project root ===
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

# === 1. Read in the three cleaned datasets ===
edu_df      = pd.read_csv("Data/Processed/cleaned_education.csv")
vax_df      = pd.read_csv("Data/Processed/cleaned_vaccination.csv")
urban_df    = pd.read_csv("Data/Processed/cleaned_urban.csv")

# === 2. Merge them all on 'State' ===
merged_df = (
    edu_df
    .merge(vax_df,   on="State", how="inner")
    .merge(urban_df, on="State", how="inner")
)

# === 3. (Optional) Drop any rows with missing data ===
# merged_df = merged_df.dropna()

# === 4. Sort alphabetically by State ===
merged_df = merged_df.sort_values(by="State", ascending=True)

# === 5. Save to CSV ===
merged_df.to_csv("Data/Processed/merged_data.csv", index=False)

print("Merge complete! Saved to Data/Processed/merged_data.csv")
