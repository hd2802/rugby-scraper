import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    team = (url.replace("https://en.wikipedia.org/wiki/", "").replace("_", " ").replace("F.C.", '').replace("Rugby", "")).strip()
    team = team.split('#', 1)[0]
    if(team == 'Harlequin'):
        team = "Harlequins"
    #print(team)

    current_squad_header = soup.find(id="Current_squad")

    if not current_squad_header:
        current_squad_header = soup.find(id="Senior_squad")

    if not current_squad_header:
        current_squad_header = soup.find(id="Current_players")

    player_data = []

    if current_squad_header:
        squad_tables = current_squad_header.find_all_next('table', class_='wikitable')[:2]
        if squad_tables:
            for squad_table in squad_tables:
                for row in squad_table.find_all('tr')[1:]: 
                    cols = row.find_all('td')

                    if cols:
                        obj = {}
                        name_cell = cols[0]
                        
                        links = name_cell.find_all('a')
                        for name_link in links:

                            if not '[' in str(name_link):
                                name = str(name_link.text.strip())
                                first_name = name.split()[0]
                                last_name = " ".join(name.split()[1:]).replace('(c)', '').replace('[c]','').replace('*','')
                                if len(first_name) > 3 and len(last_name) > 3:
                                    obj["first_name"] = first_name
                                    obj["last_name"] = last_name
                                else:
                                    continue
                            else:
                                continue
                            obj["position"] = str(cols[1].find('a').text.strip())
                            obj['team'] = team.strip()
                            player_data.append(obj)
                            

        else:
            print("Could not find squad table.")
        
    else:
        print("Could not find 'Current squad' section.")
    
    return player_data