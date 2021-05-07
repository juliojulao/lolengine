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
            return self.ranked_stats

    def showRecentMatches(self):
        last_match = self.recent_matches['matches'][:5]
        match_list = []
        for i in last_match:
            match_detail = watcher.match.by_id(self.region, i['gameId'])

            participants = []
            for i,row in enumerate(match_detail['participants']):
                participants_row = {}
                # print(row['participantId'], match_detail["participantIdentities"][int(row['participantId']-1)]['participantId'])
                # if int(row['participantId']) ==  match_detail["participantIdentities"][int(row['participantId']-1)]['participantId']:
                participants_row['Summoner Name'] = match_detail["participantIdentities"][int(row['participantId']-1)]['player']['summonerName']
                participants_row['Champion'] = championName(watcher, champ_dict, row['championId'])
                participants_row['Summ 1'] = ssName(watcher, summs_dict, row['spell1Id'])
                participants_row['Summ 2'] = ssName(watcher, summs_dict, row['spell2Id'])
                if row['stats']['win'] == True:
                    participants_row['Win'] = 'Win'
                else:
                    participants_row['Win'] = 'Loss'
                participants_row['K'] = row['stats']['kills']
                participants_row['D'] = row['stats']['deaths']
                participants_row['A'] = row['stats']['assists']
                participants_row['Damage Dealt'] = row['stats']['totalDamageDealt']
                participants_row['Gold'] = row['stats']['goldEarned']
                participants_row['Champ Lvl'] = row['stats']['champLevel']
                participants_row['CS'] = row['stats']['totalMinionsKilled']
                participants_row['Item 1'] = itemName(watcher, items_dict, row['stats']['item0'])
                participants_row['Item 2'] = itemName(watcher, items_dict, row['stats']['item1'])
                participants_row['Item 3'] = itemName(watcher, items_dict, row['stats']['item2'])
                participants_row['Item 4'] = itemName(watcher, items_dict, row['stats']['item3'])
                participants_row['Item 5'] = itemName(watcher, items_dict, row['stats']['item4'])
                participants_row['Item 6'] = itemName(watcher, items_dict, row['stats']['item5'])
                participants_row['Trinket'] = itemName(watcher, items_dict, row['stats']['item6'])
                participants.append(participants_row)
            df = pd.DataFrame(participants)
            print()
            # print(tabulate(df, showindex=False, headers=df.columns))
            print('\n')
            # print(df.to_string())
            # print(participants)
            # match_list.append(participants)
            match_list.append(df.to_html)
        return match_list