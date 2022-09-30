from django import urls
from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = urls.reverse('index')
        self.assertEquals(url, '/')
    
    def test_lista_url(self):
        url = urls.reverse('proyectos')
        self.assertEquals(url, '/proyectos/')

    def test_crear_url(self):
        url = urls.reverse('nuevo')
        self.assertEquals(url, '/nuevo/')

    def test_detalle_url(self):
        url = urls.reverse('detalle', args=[1])
        self.assertEquals(url, '/proyectos/1')
    
    def test_eliminar_proyecto_url(self):
        url = urls.reverse('eliminar', args=[1])
        self.assertEquals(url, '/1/')
    
    def test_salir_url(self):
        url = urls.reverse('salir')
        self.assertEquals(url, '/salir/')
    
    
