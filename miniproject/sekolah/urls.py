from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GuruViewSet, SiswaViewSet

router = DefaultRouter()
router.register(r'siswa', SiswaViewSet, basename='data-siswa')
router.register(r'guru', GuruViewSet, basename='data-guru')

urlpatterns = [
    path('', include(router.urls))
]