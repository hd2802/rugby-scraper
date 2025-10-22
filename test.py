with open("player_data.txt") as file:
    string = file.read()
    lines = string.splitlines()
    print((lines[lines.index('Feyi-Waboso, I')+1].split("£"))[1].split('m')[0])

