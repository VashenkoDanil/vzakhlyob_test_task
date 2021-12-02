from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsOwnerStoryOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.author == request.user or request.user.is_superuser)


class IsOwnerEpisodeOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.story.author == request.user or request.user.is_superuser)
