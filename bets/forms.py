from django import forms
from .models import bet_db

class BetAddForm(forms.ModelForm):


    class Meta:
        model = bet_db
        fields= ["sport", "tournament", "team1", "team2", "bet", "odd", "amount", "result", "return_bet", "betting_company"]
