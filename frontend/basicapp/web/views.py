from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
import requests
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'web/home.html')

@cache_page(60 * 15)
def usuarios(request):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/'
    print(f'Getting {base_url+path}')
    response = requests.get(base_url+path)
    employee_data = response.json()
    context = {
        'employees': employee_data,        
    }
    print(context)
    return render(request, 'web/usuarios.html', context)

@cache_page(60 * 15)
def detalhes(request, usuario_id):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/' + str(usuario_id)
    print(f'Getting {base_url+path}')
    response = requests.get(base_url+path)
    employee_data = response.json()
    context = {
        'employee': employee_data,        
    }
    print(context)
    return render(request, 'web/detalhes.html', context)

    def delete(request, usuario_id):
    base_url = settings.API_URL
    path = '/employee/' + str(usuario_id) + "/"

    requests.delete(base_url+path)

    return redirect("web:usuarios")