from django.urls import path

from app_blogs.views import BlogsListView, BlogDetailView

app_name = 'blogs'


urlpatterns = [
    path('', BlogsListView.as_view(), name='list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),

]











