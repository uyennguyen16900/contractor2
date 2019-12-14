import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from pet.models import Pet
from django.urls import reverse


# Create your tests here.
class PetTestCase(TestCase):
    def test_page_slugify_on_save(self):
        """ Test the slug generated when saving a Page """
        # Create and save Page to DB
        # Create a user for this test
        user = User()
        user.save()

        pet = Pet(name="Koi", breed="corgi", description="test", owner=user)
        pet.save()

        self.assertEqual(pet.slug, 'koi-corgi')

class CreatePetTest(TestCase):
    """ Tests that the wiki page creation form loads when visiting /create """
    def test_get_form(self):
        response = self.client.get('/pet/add/')

        self.assertEqual(response.status_code, 200)
