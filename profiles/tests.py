from django.test import Client, TestCase
from django.urls.base import reverse
from .models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="User Test",
            first_name="User",
            last_name="Test",
            email="user.test@test.com",
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city="Test City"
            )

    def test_should_check_profile_model(self):
        user_profile = Profile.objects.get(user__username="User Test")
        assert str(user_profile.favorite_city) == "Test City"
        assert str(user_profile) == "User Test"
        assert Profile.objects.count() == 1

    def test_should_check_index_view(self):
        uri = reverse('profiles:index')
        response = self.client.get(uri)
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertEqual(200, response.status_code)
        self.assertIn("<title>Profiles</title>", content)

    def test_should_check_profile_view(self):
        uri = reverse('profiles:profile', args=[self.profile.user.username])
        response = self.client.get(uri)
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(200, response.status_code)
        self.assertIn("<title>User Test</title>", content)
        self.assertIn("<p>Favorite city: Test City</p>", content)
