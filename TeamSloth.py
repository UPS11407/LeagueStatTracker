#import statements
#base python library. No need to pip install
import csv
import os
import configparser

#try is for if it hasn't been installed from pip
#if the try doesn't pass then the except statement installs the pip package and then imports the libraries
try:
    from riotwatcher import LolWatcher, ApiError
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'riotwatcher'])
    from riotwatcher import LolWatcher, ApiError

#config file reader
#built in python library
configParser = configparser.RawConfigParser() 
configParser.read("Config.txt", encoding="UTF-8")
configInfo = configParser["StatsConfig"]

#api info setup
#region needs 2 variables because some api requests use na1 and others use americas for some reason
#check riot documentation to see which is needed to be used when
api_key = configInfo["RGAPI-Key"]
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
#try statements are so that API errors don't throw errors and crash the program
class Top():
    name = configInfo["TopLane"]
    try:
        ID = watcher.summoner.by_name(_regionNA1, configInfo["TopLane"])["puuid"]
    except ApiError as err:
        ID = ""
        if err.response.status_code == 404:
            print("Top Laner name does not exist on NA servers. Proceeding anyways")
        elif err.response.status_code == 429:
            print("Your API key has reached the rate limit. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
        elif err.response.status_code == 403:
            print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
            os.system('pause')
            os._exit(1)
        else:
            print("Unknown error. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class JG():
    name = configInfo["Jungle"]
    try:
        ID = watcher.summoner.by_name(_regionNA1, configInfo["Jungle"])["puuid"]
    except ApiError as err:
        ID = ""
        if err.response.status_code == 404:
            print("Jungler name does not exist on NA servers. Proceeding anyways")
        elif err.response.status_code == 429:
            print("Your API key has reached the rate limit. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
        elif err.response.status_code == 403:
            print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
            os.system('pause')
            os._exit(1)
        else:
            print("Unknown error. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class Mid():
    name = configInfo["MidLane"]
    try:
        ID = watcher.summoner.by_name(_regionNA1, configInfo["MidLane"])["puuid"]
    except ApiError as err:
        ID = ""
        if err.response.status_code == 404:
            print("Mid Laner name does not exist on NA servers. Proceeding anyways")
        elif err.response.status_code == 429:
            print("Your API key has reached the rate limit. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
        elif err.response.status_code == 403:
            print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
            os.system('pause')
            os._exit(1)
        else:
            print("Unknown error. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class ADC():
    name = configInfo["BotLane"]
    try:
        ID = watcher.summoner.by_name(_regionNA1, configInfo["BotLane"])["puuid"]
    except ApiError as err:
        ID = ""
        if err.response.status_code == 404:
            print("Bot Laner name does not exist on NA servers. Proceeding anyways")
        elif err.response.status_code == 429:
            print("Your API key has reached the rate limit. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
        elif err.response.status_code == 403:
            print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
            os.system('pause')
            os._exit(1)
        else:
            print("Unknown error. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
    num=0
    full = []
    kills = 0
    assists = 0
    deaths = 0
    visionScore = 0
    damagePerMinute = 0
    goldPerMinute = 0
    playing = False

class Supp():
    name = configInfo["Support"]
    try:
        ID = watcher.summoner.by_name(_regionNA1, configInfo["Support"])["puuid"]
    except ApiError as err:
        ID = ""
        if err.response.status_code == 404:
            print("Support name does not exist on NA servers. Proceeding anyways")
        elif err.response.status_code == 429:
            print("Your API key has reached the rate limit. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
        elif err.response.status_code == 403:
            print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
            os.system('pause')
            os._exit(1)
        else:
            print("Unknown error. Please try again in 5 seconds")
            os.system('pause')
            os._exit(1)
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
            "name": Top.name,
            "Played?": Top.playing,
            "kills": Top.kills,
            "assists": Top.assists,
            "deaths": Top.deaths,
            "visionScore": Top.visionScore,
            "damagePerMinute": Top.damagePerMinute,
            "goldPerMinute": Top.goldPerMinute
        },
        {
            "name": JG.name,
            "Played?": JG.playing,
            "kills": JG.kills,
            "assists": JG.assists,
            "deaths": JG.deaths,
            "visionScore": JG.visionScore,
            "damagePerMinute": JG.damagePerMinute,
            "goldPerMinute": JG.goldPerMinute
        },
        {
            "name": Mid.name,
            "Played?": Mid.playing,
            "kills": Mid.kills,
            "assists": Mid.assists,
            "deaths": Mid.deaths,
            "visionScore": Mid.visionScore,
            "damagePerMinute": Mid.damagePerMinute,
            "goldPerMinute": Mid.goldPerMinute
        },
        {
            "name": ADC.name,
            "Played?": ADC.playing,
            "kills": ADC.kills,
            "assists": ADC.assists,
            "deaths": ADC.deaths,
            "visionScore": ADC.visionScore,
            "damagePerMinute": ADC.damagePerMinute,
            "goldPerMinute": ADC.goldPerMinute
        },
        {
            "name": Supp.name,
            "Played?": Supp.playing,
            "kills": Supp.kills,
            "assists": Supp.assists,
            "deaths": Supp.deaths,
            "visionScore": Supp.visionScore,
            "damagePerMinute": Supp.damagePerMinute,
            "goldPerMinute": Supp.goldPerMinute
        }
    ]

    with open(f"{_id}.csv", "w", encoding="UTF8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print("Information has finished being distributed to the CSV file. Thank you")
    print(f"You can find the file at {os.getcwd()}")


#matchID
_id = configInfo["GameID"]
_id = "NA1_"+_id

#full match info
#try to find it, if GameID is not real then this returns
#also checks for API key rate limiting
try:
    match = watcher.match.by_id(_regionAmericas, _id)
except ApiError as err:
    if err.response.status_code == 404:
        print("That Game ID does not exist. Please enter a valid GameID in \"Config.txt\"")
        os.system('pause')
        os._exit(1)
    elif err.response.status_code == 429:
        print("Your API key has reached the rate limit. Please try again in 5 seconds")
        os.system('pause')
        os._exit(1)
    elif err.response.status_code == 403:
        print("Your API key has expired or is blacklisted. Please update the key in \"config.txt\"")
        os.system('pause')
        os._exit(1)
    else:
        print("Unknown error. Please try again in 5 seconds")
        os.system('pause')
        os._exit(1)

count = 0

#this gives the index value of each player so that the stats are in the correct spot. Generally Top is either 0 or 5 depending on red/blue side
for i in match["metadata"]["participants"]:
    if i == Top.ID:
        Top.num = count
        Top.playing = True
    elif i == JG.ID:
        JG.num = count
        JG.playing = True
    elif i == Mid.ID:
        Mid.num = count
        Mid.playing = True
    elif i == ADC.ID:
        ADC.num = count
        ADC.playing = True
    elif i == Supp.ID:
        Supp.num = count
        Supp.playing = True
    count+=1

#this can probably be done better... I'm tired
if Top.playing:
    Top.full = match["info"]["participants"][Top.num]
    UpdateVals(Top, Top.full["kills"], Top.full["assists"], Top.full["deaths"], Top.full["visionScore"], Top.full["challenges"]["damagePerMinute"], Top.full["challenges"]["goldPerMinute"])

if JG.playing:
    JG.full = match["info"]["participants"][JG.num]
    UpdateVals(JG, JG.full["kills"], JG.full["assists"], JG.full["deaths"], JG.full["visionScore"], JG.full["challenges"]["damagePerMinute"], JG.full["challenges"]["goldPerMinute"])

if Mid.playing:
    Mid.full = match["info"]["participants"][Mid.num]
    UpdateVals(Mid, Mid.full["kills"], Mid.full["assists"], Mid.full["deaths"], Mid.full["visionScore"], Mid.full["challenges"]["damagePerMinute"], Mid.full["challenges"]["goldPerMinute"])

if ADC.playing:
    ADC.full = match["info"]["participants"][ADC.num]
    UpdateVals(ADC, ADC.full["kills"], ADC.full["assists"], ADC.full["deaths"], ADC.full["visionScore"], ADC.full["challenges"]["damagePerMinute"], ADC.full["challenges"]["goldPerMinute"])

if Supp.playing:
    Supp.full = match["info"]["participants"][Supp.num]
    UpdateVals(Supp, Supp.full["kills"], Supp.full["assists"], Supp.full["deaths"], Supp.full["visionScore"], Supp.full["challenges"]["damagePerMinute"], Supp.full["challenges"]["goldPerMinute"])

WriteCSV()
os.system('pause')