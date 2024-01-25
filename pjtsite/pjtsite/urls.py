from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include('pjtapp.urls', namespace="pjtapp")),

]

urlpatterns += staticfiles_urlpatterns()