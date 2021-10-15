from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView

from apps.api.serializers import PixabayImagesQueryParamsSerializer, PixabayImagesSerializer
from apps.api.service import PixabaySearchImages


class SearchImagesView(APIView):
    def get(self, request, format=None) -> Response:
        serializer_query_params = self._serializer_query_params(request.query_params)
        pixabay_images = PixabaySearchImages()(**serializer_query_params)
        return Response(PixabayImagesSerializer(pixabay_images.get('hits'), many=True).data)

    def _serializer_query_params(self, query_params) -> ReturnDict:
        serializer_query_params = PixabayImagesQueryParamsSerializer(data=query_params)
        serializer_query_params.is_valid(raise_exception=True)
        return serializer_query_params.data
