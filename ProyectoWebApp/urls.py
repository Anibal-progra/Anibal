from django.urls import path

from ProyectoWebApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.home, name="Home"),
    path('notostros',views.nosotros, name="Nosotros"),
    path('noticias',views.noticias, name="Noticias"),
    path('contacto',views.contacto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
