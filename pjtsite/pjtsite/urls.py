from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pjtapp.urls', namespace="pjtapp")),
    path('uploadorders/', include('pjtapp.urls', namespace="uploadorders")),
]

urlpatterns += staticfiles_urlpatterns()