from django.contrib import admin
from django.urls import path, include
from apps.views import home, api, apidjangorest
from apps.views import UsuariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('api/', api),
    path('apidjangorest/', include(router.urls)),
]
