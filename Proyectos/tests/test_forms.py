from django.test import TestCase
from Proyectos.forms import ProyectoForm
from django.contrib.auth import get_user_model

class TestForms(TestCase):

    def test_proyecto_form_valid_data(self):
        user = get_user_model().objects.create_user(
            username='testuser',
        )
        form = ProyectoForm(data={
            'nombre': 'test',
            'scrum': user
        })
        self.assertTrue(form.is_valid())

    def test_proyecto_form_no_data(self):
        form = ProyectoForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)