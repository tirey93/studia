# 2. Mamy do despozycji plik baseball.txt
# Należy wyświetlić wszystkich zawodnikaów z drużyny 'OAK'
# Którzy zawodnicy zdobyli największą ilość punktów (pole - run)?
# Którzy zawodnicy zdobyli największą ilość punktów średnio w jednym meczu (run/games)?
from zad01 import trim_line

class Baseball:
    firstname:str
    lastname:str
    age:int
    team:str
    games:int
    at_bats:int
    runs:int
    hits:int
    doubles:int
    triples:int
    homeruns:int
    RBIs:int
    walks:int
    strikeouts:int
    bat_ave:float
    on_base_pct:float
    slugging_pct:float
    stolen_bases:int
    caught_stealing:int
def from_line(line:str):
    result = Baseball()
    splitted = trim_line(line)

    result.firstname = splitted[0].strip()
    result.lastname = splitted[1].strip()
    result.age = int(splitted[2])
    result.team = splitted[3].strip()
    result.games = int(splitted[4])
    result.at_bats = int(splitted[5])
    result.runs = int(splitted[6])
    result.hits = int(splitted[7])
    result.doubles = int(splitted[8])
    result.triples = int(splitted[9])
    result.homeruns = int(splitted[10])
    result.RBIs = int(splitted[11])
    result.walks = int(splitted[12])
    result.strikeouts = int(splitted[13])
    result.bat_ave = float(splitted[14])
    result.on_base_pct = float(splitted[15])
    result.slugging_pct = float(splitted[16])
    result.stolen_bases = int(splitted[17])
    result.caught_stealing = int(splitted[18])

    return result
    
with open("baseball.txt","r") as file:
    max = 0
    max_players = []
    avg = 0.0
    avg_players = []

    next(file)
    for line in file:
        baseball = from_line(line)
        if baseball.team == "OAK":
            print(f"{baseball.firstname} {baseball.lastname}, {baseball.age} - {baseball.team}")
        if max < baseball.runs:
            max = baseball.runs
            max_players = []
        if baseball.runs == max:
            max_players.append(baseball)
        current_avg = baseball.runs / baseball.games
        if avg < current_avg and baseball.games > 10:
            avg = current_avg
            avg_players = []
        if current_avg > avg - 0.1 and baseball.games > 10:
            avg_players.append(baseball)

    print()
    for player in max_players:
        print(f"{player.firstname} {player.lastname}, {player.age}, Score: {player.runs} - {player.team}")
    print()
    for player in avg_players:
        print(f"{player.firstname} {player.lastname}, {player.age}, Score: {player.runs}, Avg: {(player.runs / player.games)} - {player.team}")
