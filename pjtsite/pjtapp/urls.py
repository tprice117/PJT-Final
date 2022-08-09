# from msilib.schema import ListView
from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import TemplateView, ListView
# from pjtapp.views import homeListView

app_name = 'pjtapp'
urlpatterns = [
    # path('', homeListView.as_view()), 
    # isnt working correctly ^
    path('', views.home, name="home"),

    path('uploadorders/', views.uploadorders, name="uploadorders"),
    path('uploadprintdata/', views.uploadprintdata, name="uploadprintdata"),
    path('details/', views.details, name="details"),
    path('summary/', views.summary, name="summary"),


]

