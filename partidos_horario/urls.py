from django.urls import path, include 
from rest_framework.documentation  import include_docs_urls
from rest_framework import routers
<<<<<<< HEAD
from .views import PartidoView

router = routers.DefaultRouter()

=======
from .views import HorarioView, PartidoView

router = routers.DefaultRouter()
router.register(r'horario',HorarioView, 'horario')
>>>>>>> 0d6c3cac974086b0c22aab65866da3557ddd972b
router.register(r'partido',PartidoView, 'partido')




urlpatterns = [
    path('',include(router.urls) ),
<<<<<<< HEAD
    path('docs/',include_docs_urls(title='Partido Api')),
=======
    path('docs/',include_docs_urls(title='Horario,Partido Api')),
>>>>>>> 0d6c3cac974086b0c22aab65866da3557ddd972b

]
