from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('Prescricacao.urls', namespace= 'Prescricacao')),
    url(r'^admin/', admin.site.urls),
]
