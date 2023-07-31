from django.test import TestCase
from django.urls import reverse
from .models import Task


# unit test
class TaskModelTests(TestCase):
    def test_str_representation(self):
        task = Task.objects.create(title='Test Task', description='테스트하기 위한 나의 task')
        # assertion()은 내가 원하는 테스트 케이스가 잘 돌아가는지 확인하는 TestCase의 함수이다
        self.assertEqual(str(task), 'Test Task')
        
    def test_str_representation2(self):
        task = Task.objects.create(title='ㄴㅇㄹㄹㄴ미ㅓㅁㄴㅇ라ㅣㄴ어ㅏㄹsdfklasdfjejwkrwlskadfjㅁㄴ이라ㅓ낭런마ㅣ어라ㅣasdlkfjsdf.a,.d21j2kl34123985', description='테스트하기 위한 나의 task')
        self.assertEqual(str(task), 'ㄴㅇㄹㄹㄴ미ㅓㅁㄴㅇ라ㅣㄴ어ㅏㄹsdfklasdfjejwkrwlskadfjㅁㄴ이라ㅓ낭런마ㅣ어라ㅣasdlkfjsdf.a,.d21j2kl34123985')
        
class TaskViewTests(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_list.html')
    
    def test_task_detail_view(self):
        task = Task.objects.create(title='Test1', description='test111111')
        response = self.client.get(reverse('task_detail', args=(task.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_detail.html')
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'test111111')
        
    def test_task_create_view(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_create.html')
        
        data = {
            'title': 'Test2',
            'description': 'this is my test case2'
        }
        
        response = self.client.post(reverse('task_create'), data)
        self.assertEqual(response.status_code, 302) # redirect == 302
        self.assertEqual(Task.objects.count(), 1)
        
    def test_task_update_view(self):
        task = Task.objects.create(title='update', description='update test')
        response = self.client.get(reverse('task_update', args=(task.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task_update.html')
        self.assertEqual(task.title, 'update')
        self.assertEqual(task.description, 'update test')
        
        update_data = {
            'title': 'update title',
            'description': 'update description'
        }
        
        response = self.client.post(reverse('task_update', args=(task.pk,)), update_data)
        self.assertEqual(response.status_code, 302)
        
        task.refresh_from_db()
        self.assertEqual(task.title, 'update title')
        self.assertEqual(task.description, 'update description')
        
    def test_task_delete_view(self):
        task = Task.objects.create(title='delete', description='delete test')
        self.assertEqual(Task.objects.count(), 1)
        response = self.client.post(reverse('task_delete', args=(task.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)