# Generated by Django 4.2.4 on 2023-09-12 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bet_db',
            options={'verbose_name_plural': 'bets'},
        ),
        migrations.AddField(
            model_name='bet_db',
            name='betting_company',
            field=models.CharField(blank=True, default='BuddyBet', max_length=30),
        ),
        migrations.AddField(
            model_name='bet_db',
            name='return_bet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bet_db',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bet_db',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bet_db',
            name='result',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='transactions_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_transaction', models.DateField(auto_now_add=True)),
                ('deposit', models.BooleanField(default=False)),
                ('withdraw', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='balance_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'balance',
            },
        ),
    ]