from dataclasses import dataclass, field

import requests
from django.conf import settings


@dataclass
class PixabaySearchImages:
    """ Pixabay API documentation https://pixabay.com/api/docs/"""
    url: str = field(init=False)

    def __post_init__(self) -> None:
        self.url = settings.PIXABAY_URL

    def __call__(self, *args, **kwargs) -> dict:
        params = {
            'key': settings.PIXABAY_KEY,
            **kwargs
        }
        response = requests.get(self.url, params=params)
        return response.json()
