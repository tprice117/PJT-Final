# from msilib.schema import ListView
from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


# from pjtapp.views import homeListView


app_name = 'pjtapp'
urlpatterns = [
    # path('', homeListView.as_view()), 
    # isnt working correctly ^
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),

    path('uploadorders/', views.uploadorders, name="uploadorders"),
    path('success/', views.success, name="success"),

    path('uploadprintdata/', views.uploadprintdata, name="uploadprintdata"),
    url(r'^details/(?P<orderid>\w+)/$', views.details, name="details"),
    url('update/<string:filename>/', views.detailsUpdate, name="detailsUpdate"),

    # path('details2/', views.details2, name="details2"),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
