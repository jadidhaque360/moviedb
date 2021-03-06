from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import MovieViewSet

router = SimpleRouter()
router.register('movies', MovieViewSet)
urlpatterns = router.urls