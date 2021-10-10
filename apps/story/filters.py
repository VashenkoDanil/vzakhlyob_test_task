from django.db.models import Q
from django_filters import FilterSet, CharFilter

from apps.story.models import Episode


class EpisodeFilter(FilterSet):
    query = CharFilter(method='filter_query_in_text_or_title_story', label='query')

    class Meta:
        model = Episode
        fields = ['query']

    def filter_query_in_text_or_title_story(self, queryset, name, value):
        return queryset.filter(Q(text__icontains=value) | Q(story__title__icontains=value))
