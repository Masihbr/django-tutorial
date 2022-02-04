from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer


class PostModelsViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
