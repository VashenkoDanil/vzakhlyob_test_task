from typing import Union, Type

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.story.filters import EpisodeFilter
from apps.story.models import Story, Episode
from apps.story.permissions import IsOwnerStoryOrReadOnly, IsOwnerEpisodeOrReadOnly
from apps.story.serializers import StorySerializer, StoryCreateUpdateSerializer, EpisodeCreateUpdateSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()

    permission_classes = [IsOwnerStoryOrReadOnly]

    def get_serializer_class(self) -> Union[Type[StoryCreateUpdateSerializer], Type[StorySerializer]]:
        if self.action in ['create', 'update']:
            return StoryCreateUpdateSerializer
        return StorySerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeCreateUpdateSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = EpisodeFilter

    permission_classes = [IsOwnerEpisodeOrReadOnly]

    def get_queryset(self) -> Episode:
        story_id = self.kwargs.get('story_id')
        if story_id:
            return Episode.objects.filter(story_id=self.kwargs.get('story_id'))
        return Episode.objects.all()
