import pandas as pd

# === 1.education data cleaning ===
edu_df = pd.read_csv("../Data/Raw/education_data.csv")
edu_df_cleaned = edu_df[['State', 'High School or Higherâ', 'Bachelors or Higher']].copy()
edu_df_cleaned.columns = ['State', 'HighSchoolOrHigher', 'BachelorsOrHigher']
edu_df_cleaned['HighSchoolOrHigher'] = edu_df_cleaned['HighSchoolOrHigher'].str.replace('%', '').astype(float)
edu_df_cleaned['BachelorsOrHigher'] = edu_df_cleaned['BachelorsOrHigher'].str.replace('%', '').astype(float)

# === 2. Vaccination Data Cleaning ===
vax_df = pd.read_csv("../Data/Raw/vaccination_data.csv")
abbr_to_name = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire',
    'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
    'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}
vax_df_cleaned = vax_df.copy()
vax_df_cleaned['State'] = vax_df_cleaned['location'].map(abbr_to_name)
vax_df_cleaned = vax_df_cleaned[['State', 'series_complete_pop_pct']].dropna()
vax_df_cleaned.rename(columns={'series_complete_pop_pct': 'VaccinationRate'}, inplace=True)

# === 3. Urbanization Data Cleaning ===
urban_df = pd.read_csv("../Data/Raw/Urban_Rural.csv")
urban_transposed = urban_df.set_index('Label (Grouping)').T
urban_transposed.columns = ['Total', 'Urban', 'Rural', 'Undefined']
urban_transposed.reset_index(inplace=True)
urban_transposed.rename(columns={'index': 'State'}, inplace=True)
urban_transposed['Total'] = urban_transposed['Total'].str.replace(',', '').astype(int)
urban_transposed['Urban'] = urban_transposed['Urban'].str.replace(',', '').astype(int)
urban_transposed['UrbanRatio'] = (urban_transposed['Urban'] / urban_transposed['Total']) * 100
urban_df_cleaned = urban_transposed[['State', 'UrbanRatio']]

# === Save Cleaned Data into designated File ===
edu_df_cleaned.to_csv("../Data/Processed/cleaned_education.csv", index=False)
vax_df_cleaned.to_csv("../Data/Processed/cleaned_vaccination.csv", index=False)
urban_df_cleaned.to_csv("../Data/Processed/cleaned_urban.csv", index=False)

print(" Data cleaning complete. Cleaned CSVs saved in Data/Processed/")
