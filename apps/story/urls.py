from django.urls import path, include
from rest_framework import routers

from .views import StoryViewSet, EpisodeViewSet

router = routers.DefaultRouter()

router.register(r'episodes', EpisodeViewSet, basename='episodes')
router.register(r'(?P<story_id>[0-9]+)/episode', EpisodeViewSet, basename='story_episodes')
router.register(r'', StoryViewSet, basename='stories')


urlpatterns = [
    path('', include(router.urls)),
]
