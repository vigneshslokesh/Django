from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_fun, name="index"),
    path("<int:month>", views.challenges_fun_num),
    path("<str:month>", views.challenges_fun, name="month-challenge") 
]