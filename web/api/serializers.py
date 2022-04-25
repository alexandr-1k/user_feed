from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.response import Response

from .models import Article

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'role', 'first_name', 'last_name')

        extra_kwargs = {'password': {'write_only': True}}


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'public', 'author')
        extra_kwargs = {'author': {'required': False}}



