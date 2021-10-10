from rest_framework import serializers


LANGUAGE_CHOICES = (
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
    ('id', 'Indonesian'),
    ('it', 'Italian'),
    ('hu', 'Hungarian'),
    ('nl', 'Dutch, Flemish'),
    ('no', 'Norwegian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ro', 'Romanian, Moldavian, Moldovan'),
    ('sk', 'Slovak'),
    ('fi', 'Finnish'),
    ('sv', 'Swedish'),
    ('tr', 'Turkish'),
    ('vi', 'Vietnamese'),
    ('th', 'Thai'),
    ('bg', 'Bulgarian'),
    ('ru', 'Russian'),
    ('el', 'Greek, Modern (1453–)'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('zh', 'Chinese'),
)

IMAGE_TYPE_CHOICES = (
    ('all', 'Все'),
    ('photo', 'Фото'),
    ('illustration', 'Иллюстрация'),
    ('vector', 'Вектор'),
)

ORIENTATION_CHOICES = (
    ('all', 'Все'),
    ('horizontal', 'По горизонтали'),
    ('vertical', 'По  вертикали')
)

CATEGORY_CHOICES = (
    ('backgrounds', 'происхождение'),
    ('fashion', 'мода'),
    ('nature', 'природа'),
    ('science', 'наука'),
    ('education', 'образование'),
    ('feelings', 'чувства'),
    ('health', 'здоровье'),
    ('people', 'люди'),
    ('religion', 'религия'),
    ('places', 'места'),
    ('animals', 'животные'),
    ('industry', 'промышленность'),
    ('computer', 'компьютер'),
    ('food', 'еда'),
    ('sports', 'спорт'),
    ('transportation', 'транспорт'),
    ('travel', 'путешествия'),
    ('buildings', 'здания'),
    ('business', 'бизнес'),
    ('music', 'музыка'),
)

COLORS_CHOICES = (
    ('grayscale', 'оттенки серого'),
    ('transparent', 'прозрачный'),
    ('red', 'красный'),
    ('orange', 'оранжевый'),
    ('yellow', 'желтый'),
    ('green', 'зеленый'),
    ('turquoise', 'бирюзовый'),
    ('blue', 'синий'),
    ('lilac', 'сиреневый'),
    ('pink', 'розовый'),
    ('white', 'белый'),
    ('gray', 'серый'),
    ('black', 'черный'),
    ('brown', 'коричневый'),
)

ORDER_CHOICES = (
    ('popular', 'популярные'),
    ('latest', 'последнии'),
)


class PixabayImagesQueryParamsSerializer(serializers.Serializer):
    """ Example params https://pixabay.com/api/docs/"""
    q = serializers.CharField(required=False)
    lang = serializers.ChoiceField(default='en', choices=LANGUAGE_CHOICES)
    id = serializers.IntegerField(required=False)
    image_type = serializers.ChoiceField(default='all', choices=LANGUAGE_CHOICES)
    orientation = serializers.ChoiceField(default='all', choices=ORIENTATION_CHOICES)
    category = serializers.ChoiceField(required=False, choices=CATEGORY_CHOICES)
    min_width = serializers.IntegerField(default=0)
    min_height = serializers.IntegerField(default=0)
    colors = serializers.ChoiceField(required=False, choices=COLORS_CHOICES)
    editors_choice = serializers.BooleanField(default=False)
    safesearch = serializers.BooleanField(default=False)
    order = serializers.ChoiceField(default='popular', choices=ORDER_CHOICES)
    page = serializers.IntegerField(default=1)
    per_page = serializers.IntegerField(min_value=3, max_value=200, default=20)

    class Meta:
        fields = [
            'q',
            'lang',
            'image_type',
            'orientation',
            'category',
            'min_width',
            'min_height',
            'colors',
            'editors_choice',
            'safesearch',
            'order',
            'page',
            'per_page',
        ]


class PreviewImagesInfo(serializers.Serializer):
    url = serializers.CharField(source='previewURL')
    width = serializers.IntegerField(source='previewWidth')
    height = serializers.IntegerField(source='previewHeight')


class WebformatImagesInfo(serializers.Serializer):
    url = serializers.CharField(source='webformatURL')
    width = serializers.IntegerField(source='webformatWidth')
    height = serializers.IntegerField(source='webformatHeight')


class LargeImagesInfo(serializers.Serializer):
    url = serializers.CharField(source='largeImageURL')
    width = serializers.IntegerField(source='imageWidth')
    height = serializers.IntegerField(source='imageHeight')
    size = serializers.IntegerField(source='imageSize')


class UserInfo(serializers.Serializer):
    user_id = serializers.IntegerField(),
    user_name = serializers.CharField(source='user')
    user_image_url = serializers.CharField(source='userImageURL')


class PixabayImagesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    page_url = serializers.CharField(source='pageURL')
    type = serializers.CharField()
    tags = serializers.CharField()
    preview_images = PreviewImagesInfo(source='*')
    webformat_images = WebformatImagesInfo(source='*')
    large_images = LargeImagesInfo(source='*')
    views = serializers.IntegerField(),
    downloads = serializers.IntegerField(),
    collections = serializers.IntegerField(),
    likes = serializers.IntegerField(),
    comments = serializers.IntegerField(),
    user = UserInfo(source='*')

    class Meta:
        fields = [
            'id',
            'pageURL',
            'type',
            'tags',
            'preview_images',
            'webformat_images',
            'large_images',
            'views',
            'downloads',
            'collections',
            'likes',
            'comments',
            'user',
        ]
