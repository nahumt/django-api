from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test """
        email = 'nahum.trinidadv@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            passsword=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
