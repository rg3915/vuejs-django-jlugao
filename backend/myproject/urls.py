from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core import views as v

router = DefaultRouter()
router.register('links/', v.LinksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
