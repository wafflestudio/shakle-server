import factory
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from factory.django import DjangoModelFactory
from rest_framework_simplejwt.tokens import RefreshToken

from circle.models import Circle, UserCircle_Member
from circle.serializers import CircleSerializer
from rest_framework import status

from user.models import User
from user.serializers import UserSignUpSerializer


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def create(cls, **kwargs):
        user = User.objects.create_user(**kwargs)
        return user


class NotMemberFactory:
    def __init__(self):
        self.user = UserFactory(
            email="notMemeber@snu.ac.kr",
            password="password",
            username="user1",
            user_id="user1",
        )


class NotManagerFactory:
    def __init__(self):
        self.user = UserFactory(
            email="notmanager@snu.ac.kr",
            password="password",
            username="user2",
            user_id="user2",
        )


class ManagerFactory:
    def __init__(self):
        self.user = UserFactory(
            email="Manager@snu.ac.kr",
            password="password",
            username="user3",
            user_id="user3",
        )


class CircleFactory(DjangoModelFactory):
    class Meta:
        model = Circle

    name = "waffle"
    bio = "wafflr_circle"
    tag = "프로그래밍"
    type0 = 0
    type1 = 0


class BoardCreateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = NotMemberFactory().user  # User1 is manager of circle
        cls.user2 = NotManagerFactory().user  # User2 is only member of circle
        cls.user3 = ManagerFactory().user  # User3 is not member of circle

        cls.circle = CircleFactory()

        UserCircle_Member.objects.create(
            circle_id=cls.circle.id, user_id=cls.user1.id, is_manager=True
        )
        UserCircle_Member.objects.create(
            circle_id=cls.circle.id, user_id=cls.user2.id, is_manager=False
        )

        cls.board_data = {"name": "QnA", "is_private": False}

        cls.user1_token = "Bearer " + str(RefreshToken.for_user(cls.user1).access_token)
        cls.user2_token = "Bearer " + str(RefreshToken.for_user(cls.user2).access_token)
        cls.user3_token = "Bearer " + str(RefreshToken.for_user(cls.user3).access_token)

    def test_create_board_success(self):
        data = self.board_data.copy()
        print(Circle.objects.all())
        token = self.user1_token
        response = self.client.post(
            f"/api/v1/circle/{self.circle.id}/board/",
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertIn("id", response_data)
        self.assertIn("name", response_data)

    def test_create_board_with_only_member_user(self):
        data = self.board_data.copy()
        token = self.user2_token
        response = self.client.post(
            f"/api/v1/circle/{self.circle.id}/board/",
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION=token,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_board_with_not_member_user(self):
        data = self.board_data.copy()
        token = self.user3_token
        response = self.client.post(
            f"/api/v1/circle/{self.circle.id}/board/",
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION=token,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
