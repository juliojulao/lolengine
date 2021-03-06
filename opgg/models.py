from django.db import models
from .utils import *
# Create your models here.


class Summoner(models.Model):
    region = models.CharField(max_length=25)
    ign = models.CharField(max_length=25)
    ranked_stats = None
    current_match = None
    recent_matches = None

    def showRank(self):
        if not self.ranked_stats:
            return "Unranked"
        else:
            self.ranked_stats['winrate'] = str(int(round(self.ranked_stats["wins"] / (self.ranked_stats["wins"] + self.ranked_stats["losses"]),2) * 100)) + '%'
            print('Rank retrieved')
            return self.ranked_stats

    def showRecentMatches(self):
        last_match = self.recent_matches[:10]
        match_list = []
        for i in last_match:
            match_detail = watcher.match.by_id("americas", i)
            participants = []
            for row in match_detail['info']['participants']:
                participants_row = {}
                participants_row['ign'] = row['summonerName']
                participants_row['region'] = self.region
                participants_row['champion'] = row['championName']
                participants_row['champId'] = row['championId']
                participants_row['ss1'] = ssName(summs_dict, row['summoner1Id'])
                participants_row['ss2'] = ssName(summs_dict, row['summoner2Id'])
                if row['win'] == True:
                    participants_row['Win'] = 'Win'
                else:
                    participants_row['Win'] = 'Loss'
                participants_row['kills'] = row['kills']
                participants_row['deaths'] = row['deaths']
                participants_row['assists'] = row['assists']
                participants_row['kda'] = f"{participants_row['kills']}/{participants_row['deaths']}/{participants_row['assists']}"
                participants_row['totaldamageDealt'] = format(row['totalDamageDealt'], ',d')
                participants_row['gold'] = format(row['goldEarned'], ',d')
                participants_row['champLevel'] = row['champLevel']
                participants_row['creepScore'] = row['totalMinionsKilled']
                participants_row['items'] = [
                    getItem(items_dict, row['item0']),
                    getItem(items_dict, row['item1']),
                    getItem(items_dict, row['item2']),
                    getItem(items_dict, row['item3']),
                    getItem(items_dict, row['item4']),
                    getItem(items_dict, row['item5']),
                    getItem(items_dict, row['item6'])
                ]
                participants.append(participants_row)

            # df = pd.DataFrame(participants)
            # print(tabulate(df, showindex=False, headers=df.columns))
            # print('\n')
            # print(df.to_string())
            match_list.append(participants)
        print('Matchlist retrieved')
        return match_list

    def showCurrentMatch(self):
        blue = 100
        red = 200
        if self.current_match == None:
            print("Summoner currently not in a match.\n")
            return
        else:
            participants = []
            for row in self.current_match['participants']:
                parts_row = {}
                parts_row['ign'] = row['summonerName']
                parts_row['region'] = self.region
                try:
                    rank = getSummonerRank(watcher, self.region, watcher.summoner.by_name(self.region,row['summonerName']))
                    parts_row['rank'] = rank['tier'] + ' ' + rank['rank']
                except TypeError:
                    parts_row['rank'] = 'Unkranked'
                parts_row['champion'] = getChampion(champ_dict, row['championId'])
                parts_row['ss1'] = ssName(summs_dict, row['spell1Id'])
                parts_row['ss2'] = ssName(summs_dict, row['spell2Id'])
                if row['teamId'] == blue:
                    parts_row['team'] = 'Blue'
                else:
                    parts_row['team'] = 'Red'
                participants.append(parts_row)
            # df = pd.DataFrame(participants)
            # print()
            # print(tabulate(df, showindex=False, headers=df.columns))
            # print('\n')
        return sorted(participants, key=lambda x: x['team'])
