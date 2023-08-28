from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status
class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso Teste 1', nivel='B'
        )
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso Teste 2', nivel='A'
        )
    # def test_fail(self):
    #     self.fail('Teste falhou de proposito')
    def teste_get_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)