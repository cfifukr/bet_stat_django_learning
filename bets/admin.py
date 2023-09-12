from django.contrib import admin
from .models import bet_db,balance_db, transactions_db


admin.site.register(bet_db)
admin.site.register(balance_db)
admin.site.register(transactions_db)