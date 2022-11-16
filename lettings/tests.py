from django.test import Client, TestCase
from django.urls.base import reverse
from .models import Address, Letting


class TestLetting(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=30,
            street="Test Street",
            city="Test City",
            state="Test State",
            zip_code=59000,
            country_iso_code=100,
            )
        cls.letting = Letting.objects.create(
            title="Letting Test",
            address=cls.address
            )

    def test_should_check_address_model(self):
        address = Address.objects.get(street="Test Street")
        assert str(address) == "30 Test Street"
        assert Address.objects.count() == 1

    def test_should_check_letting_model(self):
        letting = Letting.objects.get(title="Letting Test")
        assert str(letting.title) == "Letting Test"
        assert str(letting.address) == "30 Test Street"
        assert Letting.objects.count() == 1

    def test_should_check_index_view(self):
        uri = reverse('lettings:index')
        response = self.client.get(uri)
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertEqual(200, response.status_code)
        self.assertIn("<title>Lettings</title>", content)

    def test_should_check_letting_view(self):
        uri = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(uri)
        content = response.content.decode("utf-8")
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(200, response.status_code)
        self.assertIn("<title>Letting Test</title>", content)
        self.assertIn("<p>30 Test Street</p>", content)
