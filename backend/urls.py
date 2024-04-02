from django.contrib import admin
from django.urls import path, include

from users.views import Login, Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('torneoapp/', include('torneos.urls')),
    path('equipo_jugador/', include('equipo_jugador.urls')),
    path('partidos_horarios/', include('partidos_horario.urls')),
    path('tabla_posiciones/', include('tabla_posiciones.urls')),
    path('usuario/', include('users.api.urls')),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('refresh-token/',UserToken.as_view(),name='refresh_token'),

]