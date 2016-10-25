from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializer
from posts.util import generate_responsive_images


class PostViewSet(ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post = serializer.save(owner=self.request.user)
        generate_responsive_images.delay(post)  # manda la tarea de 'generate_responsive_images' a la cola

    def perform_update(self, serializer):
        post = serializer.save(owner=self.request.user)
        generate_responsive_images.delay(post)  # manda la tarea de 'generate_responsive_images' a la cola
