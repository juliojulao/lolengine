from .utils import *
from django.shortcuts import render, redirect
from .forms import SummonerForm
from .models import Summoner

# API_KEY = settings.RIOT_APIKEY
# watcher = LolWatcher(API_KEY)
# patch_version = json.loads(requests.get("https://ddragon.leagueoflegends.com/api/versions.json").content)[0]

# Create your views here.
def index(request,ign=None,region=None):
    if request.method == 'POST':
        summoner_form = SummonerForm(request.POST)
        if summoner_form.is_valid():
            mySummoner = Summoner()
            mySummoner.ign = summoner_form.cleaned_data['ign']
            mySummoner.region = summoner_form.cleaned_data['region']
            me = getSummoner(watcher, mySummoner.region, mySummoner.ign)
            if not me:
                print(mySummoner.ign)
                print("Empty form and url")
                summoner_form = SummonerForm()
                context = {'error': f'Summoner "{mySummoner.ign}" does not exist.', 'form': summoner_form}
                return render(request, 'opgg/opgg.html', context)
                # return redirect('/',{'form': summoner_form})
            mySummoner.ranked_stats = getSummonerRank(watcher, mySummoner.region, me)
            mySummoner.current_match = getCurrentMatch(watcher, mySummoner.region, me)
            mySummoner.recent_matches = getRecentMatches(watcher, mySummoner.region, me)
            
            print('BEFORE CONTEXT')
            context = {
                'player_info': {
                    'ign': mySummoner.ign,
                    'region': mySummoner.region,
                    'rank': mySummoner.showRank(),
                    'current_match': mySummoner.current_match,
                    'recent_matches': mySummoner.showRecentMatches(),
                },
                'form': SummonerForm(),       
            }
            print('AFTER CONTEXT')
            return render(request, 'opgg/opgg.html', context)
            # return redirect(f'/{mySummoner.region}/{mySummoner.ign}', context)

    else:
        summoner_form = SummonerForm()
        context =  {'form': summoner_form}
    return render(request, 'opgg/opgg.html', {'form': summoner_form})

# def results(request, ign, region):
#     if request.method == 'POST':
#         summoner_form = SummonerForm(request.POST)
#         if summoner_form.is_valid():
#             ign = summoner_form.cleaned_data['ign']
#             region = summoner_form.cleaned_data['region']
#             return redirect(f'/{region}/{ign}')
#     else:
#         summoner_form = SummonerForm()

#     return render(request, 'opgg/opgg.html', {'form': summoner_form})