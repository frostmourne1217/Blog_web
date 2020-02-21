from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

class HomeView(LoginRequiredMixin, ListView):
	model = Blog
	template_name = 'blog/index.html'
	context_object_name = 'blog_post'
	ordering = ['-Blog_date']
	paginate_by = 3

class ReadMore(LoginRequiredMixin, DetailView):
	model = Blog
	template_name = 'blog/read_more.html'
	
class CreateBlog(LoginRequiredMixin, CreateView):
	model = Blog
	template_name = 'blog/create_blog.html'
	fields = ['Blog_title', 'Blog_text']


	def form_valid(self,form):
		form.instance.Blog_author = self.request.user
		return super().form_valid(form)
