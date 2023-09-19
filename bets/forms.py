from django import forms
from .models import bet_db, transactions_db, balance_db

class BetAddForm(forms.ModelForm):


    class Meta:
        model = bet_db
        fields= ["sport", "tournament", "team1", "team2",
                 "bet", "odd", "amount",
                 "result", "return_bet", "live_bet",
                 "betting_company"]

class TransactionAddForm(forms.ModelForm):


    class Meta:
        model = transactions_db
        fields= ["amount", "deposit", "withdraw", "betting_company"]


class BalanceChangeForm(forms.ModelForm):


    class Meta:
        model = balance_db
        fields= ["user", "balance"]