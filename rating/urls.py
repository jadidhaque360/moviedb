from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import RatingViewSet

router = SimpleRouter()
router.register('rating', RatingViewSet)
urlpatterns = router.urls