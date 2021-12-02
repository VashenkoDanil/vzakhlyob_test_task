from rest_framework import serializers

from apps.story.models import Story, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'episode_number', 'text']


class EpisodeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    episodes = EpisodeSerializer(source='stories', many=True)

    class Meta:
        model = Story
        fields = ['id', 'title', 'author', 'cover', 'episodes']


class StoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'author', 'cover']
