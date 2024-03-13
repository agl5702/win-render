from django.urls import path, include 
from rest_framework.documentation  import include_docs_urls
from rest_framework import routers
from .views import TorneoView

router = routers.DefaultRouter()
router.register(r'torneos',TorneoView, 'torneos')





urlpatterns = [
    path('',include(router.urls) ),
    path('docs/',include_docs_urls(title='Torneo Api')),

]
