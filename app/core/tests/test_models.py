from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test """
        email = 'nahum.trinidadv@gmail.com'
        password = 'abc123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalize(self):
        """New email normalize"""
        email = 'test@CREHANAnahum.com'
        user = get_user_model().objects.create_user(email, 'nahumtrinidad')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ test invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """ Test creation new user of type superuser"""

        user = get_user_model().objects.create_superuser(
            'admin@nahum.com',
            'admin123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
