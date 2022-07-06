from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('', views.index, name='index'),
        path('jogos/', views.jogos, name='jogos'),
        path('placar_jogos/', views.placar_jogos, name='placar_jogos'),
        path('lista_jogos/', views.lista, name='lista'),
        path('pagtime/<int:time_id>', views.pagtime, name='pagtime'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)