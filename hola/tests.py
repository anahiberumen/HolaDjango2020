from django.test import TestCase

class TestSmoke(TestCase):
    def test_smoke_Test(self):
        self.assertEqual(2+2,4)

    def test_url_hola(self):
        response = self.client.get('/hola/')
        self.assertEqual(response.status_code, 200)

    def test_template_hola(self):
        response = self.client.get('/hola/')
        self.assertTemplateUsed(response, 'hola.html')
    
    def test_url_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_template_login(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_url_articulo(self):
        response = self.client.get('/articulo/')
        self.assertEqual(response.status_code, 200)

    def test_template_articulo(self):
        response = self.client.get('/articulo/')
        self.assertTemplateUsed(response, 'articulo.html')