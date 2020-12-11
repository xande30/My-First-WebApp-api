from django.test import TestCase
from django.contrib.auth import get_user_model

class Modeltests(TestCase):

    def test_create_user_with_email_successfull(self):
        """ Test creating a new user with an ermail address cuccessfull"""
        email = 'myemail@fmail.com'
        password = 'MatriX/>30{0}0'
        user = get_user_model().objects.create_user(
            email=email
            password=password
        )

    self.assertEqual(user.email, email)
    selfassertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the user of the new email is normalaized"""
        email = 'test@MATRIX.com'
        user = get_user_model().objects.create_user(email, "neo123")

        self.assertEqual(user.email, email.lower())

   def test_new_user_invalid_email(self):
       """Testing when creating a new user will give an error"""
       with self.assert.Raises(ValueError):
           get_user_model().objects.create_user(None, 'neo123')

   def test_create_a_new_superuser(self):
       """Test creating an superuser"""
       user = get_user_model().objects.create_superuser(
           'neo@matrix.com'
           'neo@matrix.com'

       )

       self.assertTrue(user.is_superuser)
       self.assertTrue(user.is_stuff)
