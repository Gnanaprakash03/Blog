from django.urls import path
from .views import (
    BlogPostView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView )


urlpatterns = [
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new', BlogCreateView.as_view(), name='post_new'), # New
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'), # New
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'), # New
]
