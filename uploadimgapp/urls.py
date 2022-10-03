from django.urls import path, include
from .views import ImageuploadModelViewSet
from rest_framework.routers import DefaultRouter

# creating Router object
router = DefaultRouter()

# Register StudentModelViewSet with router

router.register('upload',ImageuploadModelViewSet, basename='upload')

urlpatterns = [
    path('', include(router.urls)),
]
