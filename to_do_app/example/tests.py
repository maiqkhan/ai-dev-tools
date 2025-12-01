from django.test import TestCase
#from django.contrib.auth.models import User
from .models import Task, Category, User
from django.utils import timezone

#User = get_user_model()

class CategoryModelTest(TestCase):
    def test_create_category(self):
        cat = Category.objects.create(name="Work", description="Work tasks")
        self.assertIsNotNone(cat.id)
        self.assertEqual(str(cat), "Work")

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="tester", email="t@example.com", password="pass")
        self.category = Category.objects.create(name="Personal")

    def test_create_task(self):
        task = Task.objects.create(
            title="Buy milk",
            description="Buy 2 liters of milk",
            priority="medium",
            due_date=timezone.now().date(),
            category=self.category,
            user=self.user
        )
        self.assertIsNotNone(task.id)
        self.assertEqual(task.title, "Buy milk")
        self.assertFalse(task.completed)
        self.assertEqual(str(task), task.title)