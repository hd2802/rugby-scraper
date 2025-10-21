import requests
from bs4 import BeautifulSoup

positions = [
    "Props", "Hookers", "Locks", "Back row", "Fly-halves", "Scrum-halves",
    "Centres", "Fullbacks", "Wings", "Loose forwards", "Wingers"
]

non_player = [
    "Props", "Hookers", "Locks", "Back row", "Fly-halves", "Scrum-halves",
    "Centres", "Fullbacks", "^", "Bold", "Wings", "Loose forwards", "Wingers"
]

def map_position(pos): 
    if pos == 'Props':
        return "Prop"
    elif pos == "Hookers":
        return "Hooker"
    elif pos == "Locks":
        return "Lock"
    elif pos == "Back row":
        pass

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    team = url.replace("https://en.wikipedia.org/wiki/", "").replace("_", " ")
    team = team.split('#', 1)[0]
    team = team.split("(", 1)[0]
    print(team)

    player_data = []

    current_squad_header = soup.find(id="Current_squad")
    
    if current_squad_header:
        squad_tables = current_squad_header.find_next('table', class_='wikitable')
        pos_headers = squad_tables.find_all('p')

        for header in pos_headers:
            position_lists = header.find_next('ul')
            if str(header.text).strip() == "Wingers":
                position = 'Wing'
            elif str(header.text).strip() == "Loose forwards":
                position = "Back row"
            else: 
                position = str(header.text).strip().replace('ves', 'f').replace('s', '')

            for item in position_lists:
                obj = {}
                name = str(item.text).strip()
                if len(name) != 0:
                    obj["first_name"] = name.split()[0]
                    obj["last_name"] = " ".join(name.split()[1:]).replace('(c)', '').replace('[c]','').replace('*','')
                    obj['position'] = position.strip()
                    obj['team'] = team.strip()
                    player_data.append(obj)
    
    return player_data
