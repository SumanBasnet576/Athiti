from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('create/', views.create_blog_view,name='create'),
    path('<slug>/', views.detail_blog_view, name='details'),
    path('<slug>/edit/', views.edit_blog_view, name='edit'),
    path('<slug>/delete/', views.delete_post, name='delete'),
]
