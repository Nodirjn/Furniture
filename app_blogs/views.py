from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app_blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


# Create your views here.
class BlogsListView(ListView):
    template_name = ('blogs/blog-list.html')
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = BlogModel.objects.all()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        if tag:
            blogs = blogs.filter(tags=tag)
        if category:
            blogs = blogs.filter(categories=category)

        return blogs




    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)


        context['categories'] = BlogCategoryModel.objects.all()
        context['recent_blogs'] = BlogModel.objects.order_by('-created_at')[:2]
        context['tags'] = BlogTagModel.objects.all()
        return context


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        blog = self.object
        categories_id = blog.categories.values_list('id', flat=True)

        related_blogs = BlogModel.objects.filter(categories__in=categories_id).exclude(id=blog.id).distinct()[:3]
