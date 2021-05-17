import re
from .utils import *
from django.shortcuts import render, redirect
from .forms import SummonerForm
from .models import Summoner

# API_KEY = settings.RIOT_APIKEY
# watcher = LolWatcher(API_KEY)
# patch_version = json.loads(requests.get("https://ddragon.leagueoflegends.com/api/versions.json").content)[0]

# Create your views here.
def index(request,ign=None,region=None):
    print(ign, region)
    mySummoner = Summoner()
    player_data = None
    summoner_form = SummonerForm()
    if request.method == 'POST':
        print("POST REQUEST SENT")
        summoner_form = SummonerForm(request.POST)
        if summoner_form.is_valid():
            # summoner_form.save()
            mySummoner.ign = summoner_form.cleaned_data['ign']
            mySummoner.region = summoner_form.cleaned_data['region']
            return redirect(f'/{mySummoner.region}/{mySummoner.ign}')
    elif ign and region:
        print("URL REQUEST SENT")
        try:
            mySummoner.ign = ign
            mySummoner.region = region
            # player_data = getSummoner(watcher, mySummoner.region, mySummoner.ign)
        except:
            print("Region BOOM")
            return redirect('index')
    else:
        print("EMPTY PAGE REQUEST SENT")
        # summoner_form = SummonerForm()
        context =  {'form': summoner_form}
        return render(request, 'opgg/home.html', context)

    player_data = getSummoner(watcher, mySummoner.region, mySummoner.ign)
    if type(player_data) == str:
        # summoner_form = SummonerForm()
        context = {'error': player_data, 'form': summoner_form}
        return render(request, 'opgg/home.html', context)
    mySummoner.ranked_stats = getSummonerRank(watcher, mySummoner.region, player_data)
    mySummoner.current_match = getCurrentMatch(watcher, mySummoner.region, player_data)
    mySummoner.recent_matches = getRecentMatches(watcher, mySummoner.region, player_data)
    context = {
        'player_info': {
            'ign': mySummoner.ign,
            'region': mySummoner.region,
            'rank': mySummoner.showRank(),
            'current_match': mySummoner.showCurrentMatch(),
            'recent_matches': mySummoner.showRecentMatches(),
        },
        'form': summoner_form,       
    }
    print("RENDER EMPTY PAGE")
    return render(request, 'opgg/player_info.html', context)