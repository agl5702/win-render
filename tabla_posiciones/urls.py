from django.urls import path, include 
from rest_framework.documentation  import include_docs_urls
from rest_framework import routers
from .views import TablaPosicionesView, Tabla_PartidosView

router = routers.DefaultRouter()
router.register(r'Tabla-posiciones',TablaPosicionesView, 'Tabla-posiciones')
router.register(r'Tabla-partidos',Tabla_PartidosView, 'Tabla-partidos')



urlpatterns = [
    path('',include(router.urls) ),
    path('docs/',include_docs_urls(title='Tablas Api')),

]
