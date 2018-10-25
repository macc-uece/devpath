from django.test import TestCase
from django.contrib.auth.models import User
from user_manager.models import Developer

# Create your tests here.

class DevTestCase(TestCase):

    def setUp(self):
        self.user = User(
            username='test_user',
            email='test@email.com',
            password='123456',
            first_name='test',
            last_name='user'
        )
        self.user.set_password(self.user.password)

        self.dev = Developer()

    def test_developer_and_user_creation(self):
        old_users_count = User.objects.count()
        old_dev_count = Developer.objects.count()

        self.user.save()
        new_users_count = User.objects.count()
        self.assertNotEqual(old_users_count, new_users_count)

        self.dev.user = self.user
        self.dev.save()
        new_dev_count = Developer.objects.count()
        self.assertNotEqual(old_dev_count, new_dev_count)
