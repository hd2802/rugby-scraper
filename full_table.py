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

def get_player_price(first_name, last_name):
    with open("player_data.txt") as file:
        string = file.read()
        lines = string.splitlines()
        name = last_name + ", " + first_name[0]
        try:
            return ((lines[lines.index(name)+1].split("$"))[1].split('m')[0])
        except:
            return 0

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
                    first_name = name.split()[0]
                    last_name = " ".join(name.split()[1:]).replace('(c)', '').replace('[c]','').replace('*','')
                    if len(first_name) > 3 and len(last_name) > 3:
                        obj["first_name"] = first_name
                        obj["last_name"] = last_name
                    else:
                        continue
                    obj['position'] = position.strip()
                    obj['team'] = team.strip()
                    price = get_player_price(first_name, last_name)
                    if price == 0:
                        continue
                    else:
                        obj['price'] = price
                        print(obj)
                        player_data.append(obj)
    
    return player_data
