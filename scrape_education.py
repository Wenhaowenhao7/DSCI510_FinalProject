import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://worldpopulationreview.com/state-rankings/educational-attainment-by-state"

def fetch_data(n=None):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("table")
    headers = [th.text.strip() for th in table.find_all("th")]

    data_rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all("td")]
        data_rows.append(cells)
        if n and len(data_rows) >= n:
            break

    df = pd.DataFrame(data_rows, columns=headers)
    return df

def print_all():
    df = fetch_data()
    print(df.to_string(index=False))

def print_n_rows(n):
    df = fetch_data(n=n)
    print(df.to_string(index=False))

def save_to_csv(path):
    df = fetch_data()
    df.to_csv(path, index=False)
    print(f"Saved scraped data to {path}")

def main():
    parser = argparse.ArgumentParser(description="Scrape education attainment data by state.")
    parser.add_argument("--scrape", type=int, help="Only scrape the first N entries")
    parser.add_argument("--save", type=str, help="Save complete data to CSV file")

    args = parser.parse_args()

    if args.scrape:
        print_n_rows(args.scrape)
    elif args.save:
        save_to_csv(args.save)
    else:
        print_all()

if __name__ == "__main__":
    main()
