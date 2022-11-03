import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from todo.models import Project
from .views import UserModelViewSet
from users.models import User as UserApp


class TestUserViewSet(TestCase):
    def test_get_list(self):  # test Ok
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):  # test Ok
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'user_name': 'Пушкин', 'first_name': 'Пушкин', 'last_name': 'Пушкин',
                                               'email': 'testPuchkin@gmail.com'}, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):  # test Ok
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'user_name': 'Пушкин', 'first_name': 'Пушкин', 'last_name': 'Пушкин',
                                               'email': 'testPuchkin@gmail.com'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):  # test Bad
        users = User.objects.create(user_name='Пушкин', first_name='Пушкин',
                                    last_name='Пушкин', email='testPuchkin@gmail.com')

        client = APIClient()
        response = client.get(f'/api/users/{users.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):  # test Bad
        users = User.objects.create(user_name='Пушкин', first_name='Пушкин',
                                    last_name='Пушкин', email='testPuchkin@gmail.com')

        client = APIClient()
        response = client.put(f'/api/users/{users.id}/', {'name': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):  # test Bad
        users = User.objects.create(user_name='Пушкин', first_name='Пушкин',
                                    last_name='Пушкин', email='testPuchkin@gmail.com')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/users/{users.id}/', {'name': 'Грин', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        users = User.objects.get(id=users.id)
        self.assertEqual(users.name, 'Грин')
        self.assertEqual(users.birthday_year, 1880)
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):  # test Ок
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestProjectsViewSet(APITestCase):
    def test_get_list(self):  # test Ок
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):  # test Bad
        users = UserApp.objects.create(
            user_name='Роман',
            first_name='Роман',
            last_name='Роман',
            email='roman@roman.ru')
        project = Project.objects.create(
            title='TestProject',
            linkGitHub='https://github.com/RomanPM85TestProject',
            users=users)
        admin = User.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
        self.client.login(user_name='admin', password='admin')
        response = self.client.put(f'/api/projects/{project.id}/',
                                   {'title': 'ProjectAPITestCase',
                                    'linkGitHub': 'https://github.com/TestProject',
                                    'users': project.users.id
                                    })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.title, 'ProjectAPITestCase')

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        admin = UserApp.objects.create_superuser('admin', 'admin@admin.ru', 'admin')
        self.client.login(user_name='admin', password='admin')
        response = self.client.put(f'/api/projects/{project.id}/',
                                   {'title': 'ProjectMixer',
                                    'linkGitHub': 'https://github.com/ProjectMixer',
                                    'users': project.users.id
                                    })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.title, 'ProjectMixer')

    def test_get_detail(self):
        project = mixer.blend(Project, name='ProjectMixer')
        response = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['title'], 'ProjectMixer')

    def test_get_detail_users(self):
        project = mixer.blend(Project, user__title='Федор')
        response = self.client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_projects = json.loads(response.content)
        self.assertEqual(response_projects['user']['title'], 'Федор')
