from django.test import TestCase
from django.test import Client
# Create your tests here.

# Testa se o servidor está funcionando corretamente, sem nenhum problema de execução
class TestServerRunning(TestCase):
    '''Alguma descrição'''
    @classmethod
    def setUp(self):
        self.client = Client()

    def test_getIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

# Testa se todas as páginas anterior ao login estao funcionando corretamente
class TestIfAllPagesRunning(TestCase):
    '''Alguma descrição'''
    @classmethod
    def setUp(self):
        self.client = Client()

    def test_allPages(self):
        links = [
            '/',
            '/servicos',
            '/contato',
            '/user/register',
            '/user/login'
        ]
        for link in links:
            response = self.client.get(link)
            self.assertEqual(response.status_code, 200)