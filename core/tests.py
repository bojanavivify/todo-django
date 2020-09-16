from django.test import TestCase
from rest_framework.test import APIClient
from account.models import User
from .models import Todo
from .serializers import TodoSerializer


class TodoTest(TestCase):

    def setUp(self):
        self.factory = APIClient()
        self.user = User.objects.create(id=1, email='admin@gmail.com', password='sifravivify')
        self.factory.force_authenticate(user=self.user)
        self.user2 = User.objects.create(id=2, email='marko@gmail.com', password='sifravivify')

        self.todo = Todo.objects.create(id=1, title='Todo 1', description='First todo', status='To do',
                                        user=self.user)
        self.todo2 = Todo.objects.create(id=2, title='Todo 2', description='Second todo', status='To do',
                                         user=self.user)
        self.serializer = TodoSerializer(instance=self.todo2)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(["id", "title", "description",
                                                "creation_date", "status", "closed_date", "user_id"]))

    def test_todo_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['id'], self.todo2.id)
        self.assertEqual(data['title'], self.todo2.title)
        self.assertEqual(data['description'], self.todo2.description)
        self.assertEqual(data['status'], self.todo2.status)
        self.assertEqual(data['closed_date'], self.todo2.closed_date)
        self.assertEqual(data['user_id'], self.todo2.user_id)

    def create_todo(self, id_todo=3, title='Test todo', description='Test todo', status='To do'):
        return Todo.objects.create(id=id_todo, title=title, description=description, status=status,
                                   user=self.user)

    def test_model_creation(self):
        w = self.create_todo()
        self.assertTrue(isinstance(w, Todo))
        self.assertEqual(w.title, 'Test todo')

    def test_get_all(self):
        response = self.factory.get('/api/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)
        self.assertEqual(response.json()['results'][0]['title'], self.todo.title)

    def test_delete_todo(self):
        response = self.factory.delete('/api/todos/1/')
        self.assertEqual(response.status_code, 204)

        response = self.factory.get('/api/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], self.todo2.title)

    def test_update_todo(self):
        response = self.factory.patch('api/todos/2/', {"title": 'New title'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().title, 'New title')

    def test_create_todo(self):
        response = self.factory.post('api/todos/',
                                     {'title': 'Create Todo', 'description': 'Create todo',
                                      'status': 'To do', 'user': self.user}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().title, 'Create Todo')
