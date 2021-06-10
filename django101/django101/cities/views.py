from django.http import HttpResponse
from django.shortcuts import render, redirect

from django101.cities.models import Person


def index(req):
    context ={
        'name':'Doncho',
        'people': Person.objects.all()
    }
    return render(req, 'index.html', context)

def create_person(req):
    Person(
        name ='Pesho',
        age = 11,
        home_town='Sofia',
    ).save()

    return redirect('/cities')

def test_index(req):
    return HttpResponse(
        '{"name": "Doncho"}',
        content_type='application/json')


def list_phones(request):
    context = {
        'phones': [
            {
                'name': 'Galaxy S10',
                'quantity': 1,
            },
            {
                'name':'Xiaomi  MI9',
                'quantity':2,
            },
            {
                'name':'iPhone 12',
                'quantity':0,
            }
        ]
    }

    context['message'] = 'Phones list'
    return render(request, 'phones.html', context)