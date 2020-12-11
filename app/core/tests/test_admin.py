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
        """Test the user whixh are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)


   def test_user_change_page(self):
       """Test that user edit page works"""
       url = reverse('admin:core_user_change', args=[self.user.id])
       res = self.client.get(url)

       self.assertEquel(res.status_code, 200)


  def test_user_create_page(self):
      """Test that user edit page works"""
      url = reverse('admin:core_user_add')
      res = self.client.get(url)

      self.assertEquel(res.status_code, 200)
