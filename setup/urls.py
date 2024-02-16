from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('controle-geral/', admin.site.urls),
    path('', include('field_os.urls')),
]


