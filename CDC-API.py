import requests
import pandas as pd
import argparse

# CDC vaccination API (state-level)
API_URL = "https://data.cdc.gov/resource/unsk-b7fc.json"

# You can change this date if needed
TARGET_DATE = "2021-12-31T00:00:00.000"

def fetch_vaccination_data_by_date(date_str=TARGET_DATE):
    params = {
        "$select": "location,series_complete_pop_pct,date",
        "$where": f"date = '{date_str}' AND series_complete_pop_pct IS NOT NULL",
        "$limit": 1000
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)
    df["series_complete_pop_pct"] = pd.to_numeric(df["series_complete_pop_pct"], errors="coerce")
    df = df.sort_values("location").reset_index(drop=True)

    return df

def main():
    parser = argparse.ArgumentParser(description="Fetch CDC state-level vaccination data for a fixed date.")
    parser.add_argument("--save", type=str, help="Save the data to a CSV file")
    args = parser.parse_args()

    df = fetch_vaccination_data_by_date()

    if args.save:
        df.to_csv(args.save, index=False)
        print(f"✅ Data saved to {args.save}")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()
