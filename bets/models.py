from django.db import models
from django.contrib.auth.models import User

class bet_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, default = 2)
    sport  = models.CharField(max_length=30)
    team1 =  models.CharField(max_length=25, blank=True)
    team2 = models.CharField(max_length=25, blank=True)
    bet = models.CharField(max_length=25)
    odd = models.FloatField()
    amount = models.FloatField()
    result = models.BooleanField(default=False)
    return_bet = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    betting_company = models.CharField(max_length=30, blank=True, default="BuddyBet")

    class Meta:
       verbose_name_plural = "bets"

    def __str__(self):
        return self.bet + " " + self.team1 + " " + self.team2

class balance_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default= 2)
    balance = models.FloatField()
    class Meta:
       verbose_name_plural = "balance"

    def __str__(self):
        return self.user


class transactions_db(models.Model):

    amount = models.FloatField()
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE, default = 2)
    date_transaction = models.DateField(auto_now_add=True)
    deposit = models.BooleanField(default=False)
    withdraw = models.BooleanField(default=False)
    class Meta:
       verbose_name_plural = "transactions"

    def __str__(self):
        return self.amount + " " + self.date_transaction


