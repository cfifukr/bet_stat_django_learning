from django.db import models
from django.contrib.auth.models import User

class bet_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport  = models.CharField(max_length=30)
    tournament = models.CharField(max_length=50, blank = True)
    team1 =  models.CharField(max_length=25, blank=True)
    team2 = models.CharField(max_length=25, blank=True)
    bet = models.CharField(max_length=50)
    odd = models.FloatField()
    amount = models.FloatField()
    result = models.BooleanField(default=False)
    return_bet = models.BooleanField(default=False)
    live_bet = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    betting_company = models.CharField(max_length=30, blank=True, default="BuddyBet")

    class Meta:
       verbose_name_plural = "bets"

    def __str__(self):
        return str("RETURN" if self.return_bet ==  True else ["WIN" if self.result == True else "LOST"]) + " " +  self.bet + " " + "(" + self.team1 + " vs " + self.team2 + ")"

class balance_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key= True)
    balance = models.FloatField()
    class Meta:
       verbose_name_plural = "balance"

    def __str__(self):
        return str(self.user)


class transactions_db(models.Model):

    amount = models.FloatField()
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    date_transaction = models.DateField(auto_now_add=True)
    deposit = models.BooleanField(default=False)
    withdraw = models.BooleanField(default=False)
    betting_company = models.CharField(max_length=30, blank=True, default="BuddyBet")

    class Meta:
       verbose_name_plural = "transactions"

    def __str__(self):
        return str("-" if self.deposit == True else "+") + str(self.amount) + " " + str(self.date_transaction)


