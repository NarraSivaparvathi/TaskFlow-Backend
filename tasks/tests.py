
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Task


class TaskAPITests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="TestPass123!"
        )

        self.user2 = User.objects.create_user(
            username="testuser2",
            password="TestPass123!"
        )

        self.task = Task.objects.create(
            owner=self.user1,
            title="My First Task",
            description="Test task description",
            status="pending"
        )

    def authenticate_as(self, user):
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

    def test_unauthenticated_user_cannot_list_tasks(self):
        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_user_can_list_own_tasks(self):
        self.authenticate_as(self.user1)

        response = self.client.get("/api/tasks/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "My First Task")

    def test_user_cannot_view_another_users_task(self):
        self.authenticate_as(self.user2)

        response = self.client.get(
            f"/api/tasks/{self.task.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_user_cannot_update_another_users_task(self):
        self.authenticate_as(self.user2)

        response = self.client.patch(
            f"/api/tasks/{self.task.id}/",
            {"status": "completed"},
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "pending")

    def test_task_creation_assigns_logged_in_user(self):
        self.authenticate_as(self.user1)

        response = self.client.post(
            "/api/tasks/",
            {
                "title": "Automated Test Task",
                "description": "Created using an API test",
                "status": "pending"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        created_task = Task.objects.get(
            title="Automated Test Task"
        )

        self.assertEqual(created_task.owner, self.user1)