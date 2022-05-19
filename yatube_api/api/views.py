from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorPermission
from posts.models import Group, Post
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer
)


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticated,
        AuthorPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        AuthorPermission)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comments_queryset = post.comments.all()
        return comments_queryset
