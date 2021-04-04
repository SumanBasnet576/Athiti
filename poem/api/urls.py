from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    CreateComment,
    UpdateComment,
    DeleteComment,
    ShowComment,
)

urlpatterns = [
    path('', PostListView.as_view(), name='all_api'),
    path('create/', PostCreateView.as_view(), name='create_api'),
    path('<slug>/', PostDetailView.as_view(), name='detail_api'),
    path('<slug>/update/', PostUpdateView.as_view(), name='update_api'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='delete_api'),
    path('<slug>/comment/create', CreateComment.as_view(), name='comment_create'),
    path('<slug>/comment/update', UpdateComment.as_view(), name='comment_update'),
    path('<slug>/comment/', ShowComment.as_view(), name='show_comment'),
    path('<slug>/comment/delete', DeleteComment.as_view(), name='comment_delete'),
]
