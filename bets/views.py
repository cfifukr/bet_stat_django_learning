from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import BetAddForm, TransactionAddForm
from .models import balance_db, bet_db


def main_page(request):

    return render(request, 'bets/main.html')


@csrf_exempt
def sign_up_page(request):
    if request.method == "GET":
        return render(request, 'bets/sign_up.html')
    else:
        if request.POST["password1"] == request.POST["password2"]:
            data = User.objects.create_user(username=request.POST["username"], email=request.POST["email"],password=request.POST["password1"])
            data.save()
            return redirect("main_page")

        else :
            return render(request, 'bets/sign_up.html', {"error": "Password didn`t match"})

@csrf_exempt
def log_in_page(request):
    if request.method == "GET":
        return render(request, 'bets/log_in.html')
    else:
        user = authenticate(request, username = request.POST["username"], password = request.POST['password'])

        if user is None:
            return render(request, 'bets/log_in.html', {"error" : "No such a user"})
        else:
            login(request, user)
            return redirect("main_page")

@csrf_exempt
@login_required
def log_out(request):
    if request.method == "POST":
        logout(request)
    return redirect("main_page")


@csrf_exempt
@login_required
def bet_add_page(request):
    if request.method == "GET":
        data = {
            "form":BetAddForm
        }

        return render(request, 'bets/add_bet.html',data)
    else:
        bet = BetAddForm(request.POST)
        data_bet = bet.save(commit=False)
        data_bet.user = request.user
        data_bet.save()
        return redirect("bets_history_page")


@login_required
@csrf_exempt
def transaction_add_page(request):
    a = request.user
    user_balance = balance_db.objects.get(user_id = a.id)
    balance1 = float(user_balance.balance)

    if request.method == "GET":
        context = {
            "form": TransactionAddForm,
            "user_money" : balance1,


        }
        return render(request, 'bets/add_transaction.html', context)
    else:
        #transaction add
        transaction = TransactionAddForm(request.POST)
        transaction_data = transaction.save(commit=False)
        transaction_data.user = request.user
        transaction_data.save()

        #change balance
        trans_am = float(request.POST["amount"])

        user_balance.balance = float(balance1 - trans_am if transaction_data.deposit else balance1 + trans_am)
        user_balance.save()
        return redirect("main_page")


def bets_history_page(request):
    bets_data = bet_db.objects.filter(user=request.user).order_by("-date_added")

    context = {
        "bets_data": bets_data
    }
    return render(request, "bets/bets.html", context)



