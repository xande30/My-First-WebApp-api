from dhanjo.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):


    def setup(self):
        self.client = Client()
        slef.admin_user = get_user_model().onjects.create_superuser(
        email='admin@matrix.com'
        password='neo123west'
        )

        self.client.force_login(slef.admin_user)
        self.user = get_user_model().objects.create_user(
        email='test@matrix.com'
        password='neo12345west'
        name='Test user full name'
        )

    def test_user_listed(self):
        """Test the suers sre listed on user page"""
        url = reverse(admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
         
