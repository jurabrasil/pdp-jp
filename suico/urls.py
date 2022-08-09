from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('jogos/', views.jogos, name='jogos'),
        path('placar_jogos/', views.placar_jogos, name='placar_jogos'),
        path('lista/', views.lista, name='lista'),
        path('pagtime/<int:time_id>', views.pagtime, name='pagtime'),
] 