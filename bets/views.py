from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

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