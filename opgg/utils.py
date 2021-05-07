from riotwatcher import LolWatcher, ApiError
from tabulate import tabulate
from django.conf import settings
import json, requests
import pandas as pd

API_KEY = settings.RIOT_APIKEY
watcher = LolWatcher(API_KEY)
patch_version = json.loads(requests.get("https://ddragon.leagueoflegends.com/api/versions.json").content)[0]
champ_dict = watcher.data_dragon.champions(patch_version)["data"]
summs_dict = watcher.data_dragon.summoner_spells(patch_version)["data"]
items_dict = watcher.data_dragon.items(patch_version)["data"]

def getSummoner(watcher, region, ign):
    try:
        return watcher.summoner.by_name(region, ign)
    except ApiError as err:
        if err.response.status_code == 403:
            print("Invalid API key.")
        elif err.response.status_code == 404:
            print("Summoner does not exist in this region.")
        return None

def getSummonerRank(watcher, region, me):
    ranks = watcher.league.by_summoner(region, me['id'])
    for rank in ranks:
        if rank['queueType'] == 'RANKED_SOLO_5x5':
            return rank
    return None

def getCurrentMatch(watcher, region, me):
    try:
        return watcher.spectator.by_summoner(region, me['id'])
    except ApiError:
        print('Summoner currently not in a match')
        return None
    
def getRecentMatches(watcher, region, me):
    return watcher.match.matchlist_by_account(region, me['accountId'])

def itemName(watcher, items_dict, item_id):
    try:
        if item_id == 0:
            return ""
        return items_dict[str(item_id)]['name']
    except KeyError:
        return ""

def ssName(watcher, summs_dict, ss_id):
    for k,v in summs_dict.items():
        if v["key"] == str(ss_id):
            return v["name"]

def championName(watcher, champ_dict, champ_id):
    for k,v in champ_dict.items():
        if v["key"] == str(champ_id):
            return v["name"]