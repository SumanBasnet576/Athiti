from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,

)
from .permissions import UpdateOwnPost
from .pagination import MyPages
from .serializers import (
    PostSerializer,
    PostDetailSerializer,
    PostCreateAndUpdateSerializer,
    CreateCommentSerializer,
    UpdateCommentSerializer,
    DeleteCommentSerializer,
    ShowCommentSerializer,
)

from ..models import Post
from ..models import Comment


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateAndUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("title", "body",)
    pagination_class = MyPages

    permission_classes = (IsAuthenticated,)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, UpdateOwnPost,)
    serializer_class = PostCreateAndUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, UpdateOwnPost)
    serializer_class = PostSerializer
    lookup_field = 'slug'


# ========================   comments =====================

class CreateComment(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    lookup_field = 'slug'


class UpdateComment(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateCommentSerializer
    lookup_field = 'slug'


class ShowComment(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = ShowCommentSerializer
    lookup_field = 'slug'


class DeleteComment(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = DeleteCommentSerializer
    lookup_fields = 'slug'
