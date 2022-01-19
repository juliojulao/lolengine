from django import forms
from .models import Summoner

class SummonerForm(forms.ModelForm):
    class Meta:
        model = Summoner
        fields = [
            'ign',
            'region',
        ]
        REGIONS = (
            ('americas', 'NA'),
            ('europe', 'EUW'),
        )  
        widgets = {
            'ign': forms.TextInput(attrs={'class': 'search', 'placeholder': 'Summoner name'}),
            'region' : forms.Select(attrs={'class': 'search', }, choices=REGIONS),
        }
    # ign = forms.CharField(label='Summoner name', max_length=16)
    # region = forms.CharField(label="Region", max_length=16)
