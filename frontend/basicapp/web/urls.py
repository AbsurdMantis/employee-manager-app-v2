from django.urls import path
from . import views 
from django.views.decorators.cache import cache_page

app_name = 'web'
urlpatterns = [ 
        path('', views.home, name='home'), 
        path('usuarios', views.usuarios, name='usuarios'), 
        path('detalhes/<int:usuario_id>', views.detalhes, name='detalhes')
        path('detalhes/<int:usuario_id>', views.detalhes, name='detalhes')
        path('detalhes/<int:usuario_id>', views.detalhes, name='detalhes'),
        path('delete/<int:usuario_id>', views.delete, name='delete')
]