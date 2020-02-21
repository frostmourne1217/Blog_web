from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	Blog_title = models.CharField(max_length=100)
	Blog_text = models.TextField()
	Blog_date = models.DateTimeField(auto_now_add=True)
	Blog_author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.Blog_title}'
