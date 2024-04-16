# from msilib.schema import ListView
from django.urls import include, re_path, path
from django.contrib import admin
from django.views.generic import TemplateView, ListView
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import uploadorders




app_name = 'pjtapp'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('uploadorders/', views.uploadorders, name="uploadorders"),
    path('success/', views.success, name="success"),
    path('uploadorderitems/', views.uploadorderitems, name="uploadorderitems"),
    path('uploadprintmodels/', views.uploadprintmodels, name="uploadprintmodels"),
    path('uploadprintdata/', views.uploadprintdata, name="uploadprintdata"),
    re_path (r'^details/(?P<orderid>\w+)/', views.details, name="details"),
    re_path (r'update/<string:filename>/', views.detailsUpdate, name="detailsUpdate"),



] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
