# Generated by Django 4.2.4 on 2023-09-18 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0005_alter_bet_db_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions_db',
            name='betting_company',
            field=models.CharField(blank=True, default='BuddyBet', max_length=30),
        ),
    ]
