from django.test import Client, TestCase
from django.urls.base import reverse


class TestIndex(TestCase):
    def test_should_check_index_view(self):
        client = Client()
        uri = reverse('index')
        profiles_url = reverse('profiles:index')
        lettings_url = reverse('lettings:index')
        response = client.get(uri)
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(200, response.status_code)
        self.assertIn("<title>Holiday Homes</title>", content)
        self.assertIn(f"<a href=\"{profiles_url}\">Profiles</a>", content)
        self.assertIn(f"<a href=\"{lettings_url}\">Lettings</a>", content)
