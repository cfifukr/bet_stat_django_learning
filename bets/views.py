from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import BetAddForm


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
        data_bet = BetAddForm(request.POST)
        data_bet.save(commit=False)
        data_bet.user = request.user
        data_bet.save()
        return redirect("main_page")