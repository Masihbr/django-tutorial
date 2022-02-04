from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostModelsViewSet

posts_router = DefaultRouter()
posts_router.register('posts', PostModelsViewSet, basename='posts')

urlpatterns = [
    path('', include(posts_router.urls))
]
