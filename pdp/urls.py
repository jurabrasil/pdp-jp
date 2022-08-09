from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suico.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suico.urls')),
]
>>>>>>> ed7c2b00257f89ed35221e6435c1c7106ad92bb0
