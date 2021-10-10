from django.urls import path, include
from rest_framework import routers
from .views import SearchImagesView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('search-images/', SearchImagesView.as_view(), name='search_images'),
]
