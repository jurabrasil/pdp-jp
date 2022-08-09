from django.urls import path
from . import views
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0


urlpatterns = [
        path('', views.index, name='index'),
        path('jogos/', views.jogos, name='jogos'),
        path('placar_jogos/', views.placar_jogos, name='placar_jogos'),
<<<<<<< HEAD
        path('lista/', views.lista, name='lista'),
        path('pagtime/<int:time_id>', views.pagtime, name='pagtime'),
] 
=======
        path('lista_jogos/', views.lista, name='lista'),
        path('pagtime/<int:time_id>', views.pagtime, name='pagtime'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
