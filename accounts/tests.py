import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from pet.models import Pet
from django.urls import reverse

class AccountViewTests(TestCase):
    # user = User.objects.create(username='uyennguyen', password='djangopony')
    # user.save()
    def test_sign_in_page(self):
        """Test if the user is logged in after submitting the form."""
        c = self.client
        logged_in = c.login(username='uyennguyen', password='djangopony')

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        """Test if the app allows the user to sign up"""
        user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
