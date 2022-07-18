from django.urls import path
from . import views

app_name = 'pjtapp'
urlpatterns = [
    path('', views.home, name="home"),
    path('uploadorders/', views.uploadorders, name="uploadorders"),
    path('uploadprintdata/', views.uploadprintdata, name="uploadprintdata"),
    path('details/', views.details, name="details"),
    path('summary/', views.summary, name="summary"),


]

