
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.proyectos_url = reverse('proyectos')
        self.nuevo_url = reverse('nuevo')
        self.detalle_url = reverse('detalle', args=[1])
        self.eliminar_proyecto_url = reverse('eliminar', args=[1])
        self.salir_url = reverse('salir')
    
    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_lista_view(self):
        response = self.client.get(self.proyectos_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'proyecto.html')
    
    def test_crear_view(self):
        response = self.client.get(self.nuevo_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_proyecto.html')
    
    def test_salir_view(self):
        response = self.client.get(self.salir_url)
        self.assertEquals(response.status_code, 302)