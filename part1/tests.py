# part1/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Todo


class TodoAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='datta', password='datta123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_todo(self):
        data = {
            'title': 'Test Task',
            'description': 'Description',
            'status': 'OPEN',
            'tags': ['tag1', 'tag2']  # Adjusted tags format
        }

        response = self.client.post('/api/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_todo = response.data

        self.assertEqual(created_todo['title'], 'Test Task')
        self.assertEqual(created_todo['description'], 'Description')
        self.assertEqual(created_todo['status'], 'OPEN')
        self.assertEqual(
                created_todo['tags'],
                ['tag1', 'tag2']
        )


    def test_list_all_todos(self):
        response = self.client.get('/api/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todos = response.data

        self.assertIsInstance(todos, list)
        for todo in todos:
            self.assertIsInstance(todo, dict)
            self.assertIn('id', todo)
            self.assertIn('title', todo)
            self.assertIn('description', todo)
            self.assertIn('status', todo)
            self.assertIn('tags', todo)

    def test_retrieve_todo(self):
        todo = Todo.objects.create(title='Test Task', description='Description', status='OPEN', tags='tag1,tag2')

        response = self.client.get(reverse('todo-retrieve', kwargs={'pk': todo.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        retrieved_todo = response.data

        self.assertEqual(retrieved_todo['title'], 'Test Task')
        self.assertEqual(retrieved_todo['description'], 'Description')
        self.assertEqual(retrieved_todo['status'], 'OPEN')
        self.assertEqual(''.join(retrieved_todo['tags']), 'tag1,tag2')  # Compare with a string

    def test_update_todo(self):
        todo = Todo.objects.create(title='Test Task', description='Description', status='OPEN', tags='tag1,tag2')

        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'status': 'DONE',
            'tags': ['updated_tag1', 'updated_tag2']  # Adjusted tags format
        }

        update_url = reverse('todo-update', kwargs={'pk': todo.id})
        response = self.client.put(update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_todo = response.data

        self.assertEqual(updated_todo['title'], 'Updated Task')
        self.assertEqual(updated_todo['description'], 'Updated Description')
        self.assertEqual(updated_todo['status'], 'DONE')
        self.assertEqual(updated_todo['tags'], ['updated_tag1', 'updated_tag2'])  # Updated expected format

    def test_destroy_todo(self):
        todo = Todo.objects.create(title='Test Task', description='Description', status='OPEN', tags='tag1,tag2')

        response = self.client.delete(reverse('todo-destroy', kwargs={'pk': todo.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Todo.objects.filter(id=todo.id).exists())
