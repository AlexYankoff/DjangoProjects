from django.urls import path
from django.views.generic import TemplateView

from django101.cities.views import index, list_phones, create_person, test_index, show_forms_demo

urlpatterns = [
    path('',index),
    path('create/', create_person, name = 'create person'),
    path('test/', test_index),
    path('phones/', list_phones),
    path('phones2/', TemplateView.as_view(template_name='phones.html')),
    path('forms/', show_forms_demo),
]