from bs4 import BeautifulSoup
from django.test  import  TestCase ,  RequestFactory
from django.http import HttpResponse
from django.template import loader
from urllib import *
from html import *

from django.test import Client

from blog.forms import PostForm
from blog.views import *
from django.contrib.auth.models import User



# class Teste(TestCase):
#     def test(self):
#         return '<title>Blog Do Django</title>' in html

# if __name__ == '__main__':
#     main()

class PrimeiroTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.u = User.objects.create_user(
            username='javed', email='javed@javed.com', password='my_secret')
        
    def test_verificar_titulo_no_index(self):
        response = self.c.get("")
        self.assertIn('<title>Blog do Django</title>', str(response.content), 'A pagina não contem este dado')

    def test_formulario_new_valido(self):
        form_data = {'title':'Título', 'text':'Texto da postagem'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_novo_post_se_retorna_postagem(self):
        form_data = {'title':'Título', 'text':'Texto da postagem'}
        self.c.force_login(self.u)

        response = self.c.post('/post/new/', form_data, follow=True)
        self.assertNotIn('<h1>Postagem</h1>', str(response.content))

    def test_novo_post_retorna_detalhes(self):
        form_data = {'title':'Título', 'text':'Texto da Postagem 2'}
        self.c.force_login(self.u)

        response = self.c.post('/post/new/', form_data, follow=True)
        self.assertIn('<h1>Detalhes</h1>', str(response.content))


    def test_pagina_index_retorna_status_200(self):
        response = self.c.get('')
        self.assertEqual(200, response.status_code)


    def test_pagina_about_retorna_status_200(self):
        response = self.c.get('/sobre')
        self.assertEqual(response.status_code, 200)


    def test_sobre_entrada_pelo_metodo(self):
        request = 'http://127.0.0.1:8000/sobre'
        response = sobre(request)
        self.assertEqual(200, response.status_code)    

    def test_index_entrada_pelo_metodo(self):
        request = 'http://127.0.0.1:8000'
        response = index(request)
        self.assertEqual(200, response.status_code)








