from django.urls import path
from .views import index, create, refresh#, delete
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('modificar/<int:user_id>', refresh, name='modificar'),
    #path('deletar/<int:user_id>', delete, name='deletar'),
    path('admin/', admin.site.urls),
]
