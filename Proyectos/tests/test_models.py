

from unittest import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from Proyectos.models import Proyecto

class TestModels(TestCase):
    def test_proyecto_model(self):
        user = get_user_model().objects.create_user(
            username='testuser',
        )