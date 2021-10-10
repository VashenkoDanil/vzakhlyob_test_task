from django.contrib import admin

from apps.story.models import Episode, Story


class EpisodeInline(admin.TabularInline):
    model = Episode


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [
        EpisodeInline,
    ]


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
