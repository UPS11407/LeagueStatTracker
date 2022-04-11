#import statements
#base python library. No need to pip install
import csv
import os

#try is for if it hasn't been installed from pip
#if the try doesn't pass then the except statement installs the pip package and then imports the libraries
try:
    from riotwatcher import LolWatcher, ApiError
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'riotwatcher'])
    from riotwatcher import LolWatcher, ApiError

#api info setup
#region needs 2 variables because some api requests use na1 and others use americas for some reason
#check riot documentation to see which is needed to be used when
api_key = 'API-KEY'
watcher = LolWatcher(api_key)
_regionNA1 = 'na1'
_regionAmericas = "americas"

#stats we want to track
#kills
#assists
#deaths
#vision score
#damage per min
#gold per min


#each player's class
class Smae():
    ID = watcher.summoner.by_name(_regionNA1, "TSL smæ")["puuid"]
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False


class Jordan():
    ID = watcher.summoner.by_name(_regionNA1, "TSL Cease")["puuid"]
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class Tian():
    ID = watcher.summoner.by_name(_regionNA1, "NewPogChamp")["puuid"]
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class Kali():
    ID = watcher.summoner.by_name(_regionNA1, "TSL Kali")["puuid"]
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class Bluesnake():
    ID = watcher.summoner.by_name(_regionNA1, "Bluesnake")["puuid"]
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

#name is the class that is assigned to each player, rest of the params are self explanatory
def UpdateVals(name, kills, assists, deaths, visionScore, damagePerMinute, goldPerMinute):
    name.kills = kills
    name.assists = assists
    name.deaths = deaths
    name.visionScore = visionScore
    name.damagePerMinute = damagePerMinute
    name.goldPerMinute = goldPerMinute

def WriteCSV():
    headers = ["name", "Played?", "kills", "assists", "deaths", "visionScore", "damagePerMinute", "goldPerMinute"]
    rows = [
        {
            "name": "Smae",
            "Played?": Smae.playing,
            "kills": Smae.kills,
            "assists": Smae.assists,
            "deaths": Smae.deaths,
            "visionScore": Smae.visionScore,
            "damagePerMinute": Smae.damagePerMinute,
            "goldPerMinute": Smae.goldPerMinute
        },
        {
            "name": "Jordan",
            "Played?": Jordan.playing,
            "kills": Jordan.kills,
            "assists": Jordan.assists,
            "deaths": Jordan.deaths,
            "visionScore": Jordan.visionScore,
            "damagePerMinute": Jordan.damagePerMinute,
            "goldPerMinute": Jordan.goldPerMinute
        },
        {
            "name": "Tian",
            "Played?": Tian.playing,
            "kills": Tian.kills,
            "assists": Tian.assists,
            "deaths": Tian.deaths,
            "visionScore": Tian.visionScore,
            "damagePerMinute": Tian.damagePerMinute,
            "goldPerMinute": Tian.goldPerMinute
        },
        {
            "name": "Kali",
            "Played?": Kali.playing,
            "kills": Kali.kills,
            "assists": Kali.assists,
            "deaths": Kali.deaths,
            "visionScore": Kali.visionScore,
            "damagePerMinute": Kali.damagePerMinute,
            "goldPerMinute": Kali.goldPerMinute
        },
        {
            "name": "Bluesnake",
            "Played?": Bluesnake.playing,
            "kills": Bluesnake.kills,
            "assists": Bluesnake.assists,
            "deaths": Bluesnake.deaths,
            "visionScore": Bluesnake.visionScore,
            "damagePerMinute": Bluesnake.damagePerMinute,
            "goldPerMinute": Bluesnake.goldPerMinute
        }
    ]

    with open(f"{_id}.csv", "w", encoding="UTF8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print("Information has finished being distributed to the CSV file. Thank you")
    print(f"You can find the file at {os.getcwd()}")


#matchID
_id = input("Please enter the gameID")
_id = "NA1_"+_id

#full match info
match = watcher.match.by_id(_regionAmericas, _id)

count = 0

#this gives the index value of each player so that the stats are in the correct spot. Generally smae is either 0 or 5 depending on red/blue side
for i in match["metadata"]["participants"]:
    if i == Smae.ID:
        Smae.num = count
        Smae.playing = True
    elif i == Jordan.ID:
        Jordan.num = count
        Jordan.playing = True
    elif i == Tian.ID:
        Tian.num = count
        Tian.playing = True
    elif i == Kali.ID:
        Kali.num = count
        Kali.playing = True
    elif i == Bluesnake.ID:
        Bluesnake.num = count
        Bluesnake.playing = True
    count+=1

#this can probably be done better... I'm tired
if Smae.playing:
    Smae.full = match["info"]["participants"][Smae.num]
    UpdateVals(Smae, Smae.full["kills"], Smae.full["assists"], Smae.full["deaths"], Smae.full["visionScore"], Smae.full["challenges"]["damagePerMinute"], Smae.full["challenges"]["goldPerMinute"])

if Jordan.playing:
    Jordan.full = match["info"]["participants"][Jordan.num]
    UpdateVals(Jordan, Jordan.full["kills"], Jordan.full["assists"], Jordan.full["deaths"], Jordan.full["visionScore"], Jordan.full["challenges"]["damagePerMinute"], Jordan.full["challenges"]["goldPerMinute"])

if Tian.playing:
    Tian.full = match["info"]["participants"][Tian.num]
    UpdateVals(Tian, Tian.full["kills"], Tian.full["assists"], Tian.full["deaths"], Tian.full["visionScore"], Tian.full["challenges"]["damagePerMinute"], Tian.full["challenges"]["goldPerMinute"])

if Kali.playing:
    Kali.full = match["info"]["participants"][Kali.num]
    UpdateVals(Kali, Kali.full["kills"], Kali.full["assists"], Kali.full["deaths"], Kali.full["visionScore"], Kali.full["challenges"]["damagePerMinute"], Kali.full["challenges"]["goldPerMinute"])

if Bluesnake.playing:
    Bluesnake.full = match["info"]["participants"][Bluesnake.num]
    UpdateVals(Bluesnake, Bluesnake.full["kills"], Bluesnake.full["assists"], Bluesnake.full["deaths"], Bluesnake.full["visionScore"], Bluesnake.full["challenges"]["damagePerMinute"], Bluesnake.full["challenges"]["goldPerMinute"])

WriteCSV()
input("Press Enter to continue...")