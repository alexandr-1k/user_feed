from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserViewSet, ArticlesViewSet

router = DefaultRouter()
router.register('createuser', CreateUserViewSet)
router.register('articles', ArticlesViewSet, basename='article')


urlpatterns = [
    path('', include(router.urls))
]
