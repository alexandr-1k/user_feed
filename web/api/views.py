from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from web.permissions import UserPermission
from .serializers import UserSerializer, ArticleSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Article

User = get_user_model()


class CreateUserViewSet(CreateModelMixin,
                        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticlesViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return Article.objects.filter(public=True)
        return Article.objects.all()

    def create(self, request, *args, **kwargs):
        serialized_input = self.get_serializer(data=request.data)
        serialized_input.is_valid()

        article = Article(author=request.user, **serialized_input.data)
        article.save()

        return Response(self.get_serializer(article).data)
