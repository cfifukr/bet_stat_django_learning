
from django.contrib import admin
from django.urls import path
from bets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name = "main_page"),



    #auth
    path('signup/', views.sign_up_page, name = "sign_up_page")


]
