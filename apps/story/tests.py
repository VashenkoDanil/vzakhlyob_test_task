from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.account.models import User
from apps.story.models import Story


def create_temporary_image(file_name: str = 'temp_file.jpeg'):
    bts = BytesIO()
    img = Image.new('RGB', (1, 1))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile(file_name, bts.getvalue())


@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class StoryViewSetTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            'user1',
            email='user1@test.com',
            password='testing'
        )

        self.temp_file = create_temporary_image()

        self.story1 = Story.objects.create(
            title='Заголовок 1',
            author=self.user1,
            cover=self.temp_file.name
        )
        self.story2 = Story.objects.create(
            title='Заголовок 2',
            author=self.user1,
            cover=self.temp_file.name
        )
        self.result_story = [{
            'id': 1,
            'title': 'Заголовок 1',
            'author': 'user1',
            'cover': f'http://testserver/media/{self.temp_file.name}',
            'episodes': []
        }, {
            'id': 2,
            'title': 'Заголовок 2',
            'author': 'user1',
            'cover': f'http://testserver/media/{self.temp_file.name}',
            'episodes': []
        }]

    def test_story_url(self):
        path = reverse('stories-list')
        self.assertEqual(path, '/story/')

    def test_story_list(self):
        response = self.client.get(reverse('stories-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            self.result_story
        )

    def test_story_detail(self):
        response = self.client.get(reverse('stories-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            self.result_story[0]
        )

    def test_story_create(self):
        file = create_temporary_image('file.jpeg')
        data = {
            'title': 'Заголовок 3',
            'author': 1,
            'cover': file,
        }
        response = self.client.post(reverse('stories-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                'title': 'Заголовок 3',
                'author': 1,
                'cover': 'http://testserver/media/stories/file.jpeg',
            }
        )

    def test_story_update(self):
        story = Story.objects.get(pk=1)
        self.assertEqual(story.id, 1)
        self.assertEqual(story.title, 'Заголовок 1')
        self.assertEqual(story.author.id, 1)
        self.assertEqual(story.cover.name, 'temp_file.jpeg')

        response = self.client.put(
            reverse('stories-detail', kwargs={'pk': 1}),
            data={'title': 'Новый заголовок 1', 'author': 1, 'cover': create_temporary_image('new_file.jpeg')}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'title': 'Новый заголовок 1',
                'author': 1,
                'cover': 'http://testserver/media/stories/new_file.jpeg',
            }
        )

        story = Story.objects.get(id=1)
        self.assertEqual(story.id, 1)
        self.assertEqual(story.title, 'Новый заголовок 1')
        self.assertEqual(story.author.id, 1)
        self.assertEqual(story.cover.name, 'stories/new_file.jpeg')

    def test_story_deleted(self):
        response = self.client.delete(reverse('stories-detail', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Story.objects.filter(pk=2).exists())
