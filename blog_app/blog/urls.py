from django.urls import path
from .views import HomeView, ReadMore, CreateBlog
urlpatterns = [
    path('', HomeView.as_view(), name = 'blog-home'),
    path('blog/<int:pk>/', ReadMore.as_view(), name = 'read-more'),
    path('create_blog', CreateBlog.as_view(success_url='/'), name = 'create_blog')
]
