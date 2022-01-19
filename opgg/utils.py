from riotwatcher import LolWatcher, ApiError
from tabulate import tabulate
from django.conf import settings
import json, requests
import pandas as pd
import time

# Load champion, summoner spells, and items dictionaries to retrieve data later
API_KEY = settings.RIOT_APIKEY
watcher = LolWatcher(API_KEY)
patch_version = json.loads(requests.get("https://ddragon.leagueoflegends.com/api/versions.json").content)[0]
print('Downloading champion dictionary...')
start = time.time()
champ_dict = watcher.data_dragon.champions(patch_version)["data"]
end = time.time()
print(f'Time elapsed: {end - start}')

print('Downloading summs dictionary...')
start = time.time()
summs_dict = watcher.data_dragon.summoner_spells(patch_version)["data"]
end = time.time()
print(f'Time elapsed: {end - start}')

print('Downloading item dictionary...')
start = time.time()
items_dict = watcher.data_dragon.items(patch_version)["data"]
end = time.time()
print(f'Time elapsed: {end - start}')

def getSummoner(watcher, region, ign):
    try:
        return watcher.summoner.by_name(region, ign)
    except ApiError as err:
        print(err)
        if err.response.status_code == 403:
            print("Invalid API key. Please update API key.")
            return "Invalid API key. Please update API key"
        elif err.response.status_code == 404:
            print(f"Summoner \"{ign}\" does not exist in this region.")
            return f"Summoner \"{ign}\" does not exist in this region."
        elif err.response.status_code == 400:
            print("Invalid region")
            return "Invalid region."

def getSummonerRank(watcher, region, player_data):
    ranks = watcher.league.by_summoner(region, player_data['id'])
    for rank in ranks:
        if rank['queueType'] == 'RANKED_SOLO_5x5':
            return rank
    return None

def getCurrentMatch(watcher, region, player_data):
    try:
        return watcher.spectator.by_summoner(region, player_data['id'])
    except ApiError:
        print('Summoner currently not in a match')
        return None
    
def getRecentMatches(watcher, region, player_data):
    return watcher.match.matchlist_by_puuid(region, player_data['puuid'])

def getItem(items_dict, item_id):
    try:
        if item_id == 0:
            return ""
        return items_dict[str(item_id)]
    except KeyError:
        return ""

def ssName(summs_dict, ss_id):
    for k,v in summs_dict.items():
        if v["key"] == str(ss_id):
            return v

def getChampion(champ_dict, champ_id):
    for k,v in champ_dict.items():
        if v["key"] == str(champ_id):
            return v
