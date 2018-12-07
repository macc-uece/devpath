# *** EXPLICAÇÂO ***   
# existem dois metodos padroes em testes, o setUp e o tearDown
# o setUp sempre será executado antes de cada teste, nesse caso tem duas funções 
# não padroes dentro dessa classe, que são o test_add... e o test_login..., 
# ou seja, o setUp será executado duas vezes, uma vez antes de cada execução 
# de cada função citada anteriormente

# o tearDown, caso exista, será executado após cada função
# ter feito os seus testes...

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from user_manager.models import Developer

# Testa o CRUD de usuario
class TestUserServer(TestCase):
    # define um usuario antes dos testes acontecerem
    def setUp(self):
        self.user = User(
            username='jhWal',
            email='jhWal@email.com',
            password='myPassword',
            first_name='Jhon',
            last_name='Walker'
        )
        self.user.set_password(self.user.password)
        self.dev = Developer()

    # Testa se o usuario é criado corretamente
    def test_userRegister(self):
        response = self.client.post( 
            '/user/register',
            {
                'username' :'test_user',
                'email' : 'test@email.com',
                'password' : '123456',
                'first_name' : 'test',
                'last_name' : 'user' 
            }
        )
        self.assertEqual(response.status_code, 302)
        
    # Testa o login do usuario
    def test_userLogin(self):
        response = self.client.post('/user/login', { 'username' :'jhWal','password' : 'myPassword'})
        self.assertEqual(response.status_code, 200)



class TestCreateUserDatabase(TestCase):
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

    # Testa se o usuario é salvo no banco de dados
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