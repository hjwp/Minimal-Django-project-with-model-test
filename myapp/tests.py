from django.test import TestCase

from .models import Thing

# Create your tests here.
class TestModels(TestCase):

    def test_saving_a_model(self):
        thing = Thing.objects.create()
        thing.save()

        self.assertEqual(Thing.objects.all().count(), 1)
