# Generated by Django 4.2.1 on 2023-09-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_alter_balance_db_user_alter_bet_db_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet_db',
            name='tournament',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]