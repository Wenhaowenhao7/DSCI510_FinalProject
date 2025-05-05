README.txt

Project: Education and Immunization: Analyzing the Relationship Between Regional Education Levels and
COVID-19 Vaccination Rates in the U.S.

Overview:
This script (`scrape_education.py`) extracts educational attainment data by U.S. state from the website:
https://worldpopulationreview.com/state-rankings/educational-attainment-by-state

The dataset includes the following fields for each U.S. state:
- State
- % High School Graduate or Higher
- % Bachelor's Degree or Higher
- % Graduate or Professional Degree

This script is part of a broader analysis to investigate correlations between education levels and COVID-19 vaccination rates across U.S. regions.

---

Usage Instructions:

Run the script from the command line using Python 3. The script supports three modes of execution:

1. Print the entire dataset:
python scrape_education.py

2. Print only the first N entries:
python scrape_education.py --scrape 10

3. Save the data to a CSV file:
python scrape_education.py --save education_data.csv

Data Output:

Format: CSV

Default saved filename: education_data.csv

Number of entries: 51 (50 states + United States overall row)

Approximate size: <50 KB


Install python packages required by this program using:
pip install requests beautifulsoup4 pandas

Wenhao Wang Date: April 16, 2025