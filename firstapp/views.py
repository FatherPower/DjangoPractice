from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>H1</h1>') #リクエストが来たらこの値をレスポンスとして返す
    
def user_page(request,user_name):
    return HttpResponse(f'<h1>{user_name}`s page</h1>')

def number_page(request,user_name,number):
    user_name = user_name.upper()
    return HttpResponse(f'<h1>{user_name} `S number page = {number}</h1>')