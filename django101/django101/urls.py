
from django.contrib import admin
from django.urls import path, include

import django101
from django101.cities.views import index, list_phones

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('cities/',include('django101.cities.urls')),
    path('', include('django101.people.urls')),

]
