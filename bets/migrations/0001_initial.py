# Generated by Django 4.2.4 on 2023-09-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bet_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=30)),
                ('team1', models.CharField(blank=True, max_length=25)),
                ('team2', models.CharField(blank=True, max_length=25)),
                ('bet', models.CharField(max_length=25)),
                ('odd', models.FloatField()),
                ('amount', models.FloatField()),
                ('result', models.BooleanField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
