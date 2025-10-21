import cell_table
import full_table
import json

prem_urls = [ 
    "https://en.wikipedia.org/wiki/Northampton_Saints#Current_squad",
    "https://en.wikipedia.org/wiki/Bath_Rugby#Senior_squad",
    "https://en.wikipedia.org/wiki/Bristol_Bears",
    "https://en.wikipedia.org/wiki/Exeter_Chiefs",
    "https://en.wikipedia.org/wiki/Gloucester_Rugby",
    "https://en.wikipedia.org/wiki/Harlequin_F.C.",
    "https://en.wikipedia.org/wiki/Leicester_Tigers",
    "https://en.wikipedia.org/wiki/Newcastle_Red_Bulls",
    "https://en.wikipedia.org/wiki/Sale_Sharks",
    "https://en.wikipedia.org/wiki/Saracens_F.C."
]

urc_urls = [
    "https://en.wikipedia.org/wiki/Benetton_Rugby",
    "https://en.wikipedia.org/wiki/Bulls_(rugby_union)",
    "https://en.wikipedia.org/wiki/Cardiff_Rugby",
    "https://en.wikipedia.org/wiki/Connacht_Rugby",
    "https://en.wikipedia.org/wiki/Dragons_(rugby_union)",
    "https://en.wikipedia.org/wiki/Edinburgh_Rugby",
    "https://en.wikipedia.org/wiki/Glasgow_Warriors",
    "https://en.wikipedia.org/wiki/Leinster_Rugby",
    "https://en.wikipedia.org/wiki/Lions_(United_Rugby_Championship)",
    "https://en.wikipedia.org/wiki/Munster_Rugby",
    "https://en.wikipedia.org/wiki/Ospreys_(rugby_union)",
    "https://en.wikipedia.org/wiki/Scarlets",
    "https://en.wikipedia.org/wiki/Sharks_(rugby_union)",
    "https://en.wikipedia.org/wiki/Stormers",
    "https://en.wikipedia.org/wiki/Ulster_Rugby",
    "https://en.wikipedia.org/wiki/Zebre_Parma"
]

def prem_data():
    data = []

    for url in prem_urls:
        data.extend(cell_table.get_data(url))
    
    with open("prem.json", "w") as file:
        file.write(json.dumps(data, indent=4)) 
    
def urc_data():
    data = []

    for url in urc_urls:
        data.extend(full_table.get_data(url))
    
    with open('urc.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

def main():
    prem_data()
    urc_data()

if __name__ == "__main__":
    main()