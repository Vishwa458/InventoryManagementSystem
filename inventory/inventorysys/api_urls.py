from django.urls import path, include
from .views import *
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()
router.register('', LaptopViewset, basename='laptops')

urlpatterns = [
    path('', include(router.urls)),
]
