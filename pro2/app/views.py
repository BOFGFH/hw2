from django.shortcuts import render
import requests

def home(request):
    return render(request, 'myapp/home.html')

def item_list(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    items = response.json()
    return render(request, 'myapp/list.html', {'items': items})

def item_card(request, item_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{item_id}')
    item = response.json()
    return render(request, 'myapp/card.html', {'item': item})
