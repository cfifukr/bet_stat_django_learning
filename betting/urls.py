
from django.contrib import admin
from django.urls import path
from bets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name = "main_page"),
    path('bet_add/', views.bet_add_page, name = "add_bet_page"),



    #auth
    path('signup/', views.sign_up_page, name = "sign_up_page"),
    path('login/', views.log_in_page, name = "log_in_page"),
    path('logout/', views.log_out, name = "log_out_page")


]
