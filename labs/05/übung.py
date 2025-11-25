import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random



def scrape():
    data = []
    url = "https://www.scrapethissite.com/pages/forms/"
    page = 1

    while True:
        response = requests.get(f"{url}?page_num={page}")
        print(f"Starte Rquest für Seite: {page}")
        if response.status_code != 200:
            print("Abgebrochen. Status_code:", response.status_code)
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')

        team_zeilen = soup.find_all('tr', class_='team')

        if not team_zeilen:
            print("Alle TEams gescraped")
            break
        
        for row in team_zeilen:
            cells = row.find_all('td')

            name = cells[0].text.strip()
            year = cells[1].text.strip()
            wins = cells[2].text.strip()
            losses = cells[3].text.strip()
            ot_losses = cells[4].text.strip()
            pct_text_sucess = cells[5].text.strip()
            gf = cells[6].text.strip()
            ga = cells[7].text.strip()
            diff_text_sucess = cells[8].text.strip()

            data.append({
                "name": name,
                "year": year,
                "wins": wins,
                "losses": losses,
                "ot_losses": ot_losses,
                "pct_text_sucess": pct_text_sucess, 
                "gf": gf,
                "ga": ga,
                "diff_text_sucess": diff_text_sucess
            })      

        page += 1
        time.sleep(random.randint(1,3))
    return data

def save_to_csv(data):
    if data:
        df = pd.DataFrame(data)

        csv_filename = "labs/05/data.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8')
        print("Datei gespeidert")


# save_to_csv(scrape())

df = pd.read_csv("labs/05/data.csv")

df['year'] = pd.to_numeric(df['year'])
df['wins'] = pd.to_numeric(df['wins'])

jahre = [1990, 2000, 2010]

#print("\nWho made the made most wins in 1990, 2000, and 2010?: \n"+str("_"*30))
for jahr in jahre:
    df_jahr = df[df['year'] == jahr]
    idx_max_wins = df_jahr['wins'].idxmax()
    top_team = df.loc[idx_max_wins]
    #print(f"{jahr}: {top_team['name']} mit {top_team['wins']} Siegen")


print("\nHow many teams participated in 1991, 2001, and 2011?: \n"+str("_"*30))
jahre_fuer_anzahl = [1991, 2001, 2011]

for jahr in jahre_fuer_anzahl:
    df_jahr = df[df['year'] == jahr]
    anzahl_teams = len(df_jahr)
    print(f"  {jahr}: {anzahl_teams} Teams")