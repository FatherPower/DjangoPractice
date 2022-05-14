from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    value = 'good bye'
    return render(request,'app/index.html', context={'value':value})  

def home(request):
    my_name = 'taro Yamada'
    favorite_fruits = ['Apple','Grape','H']
    my_info = {
        'name':'taro',
        'age':18
    }

    return render(request, 'app/home.html', context = {
        'my_name': my_name,
        'favorite_fruits':favorite_fruits,
        'my_info' : my_info
    })
def user_page(request,user_name):
    return HttpResponse(f'<h1>{user_name}`s page</h1>')

def number_page(request,user_name,number):
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{user_name} `S number page = {number}</h1>')