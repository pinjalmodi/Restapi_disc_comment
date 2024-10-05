from django.db import models


# Create your models here.
class Discussion(models.Model):
	title=models.CharField(max_length=250,blank=False)
	content=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	author=models.CharField(max_length=100)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	discussion=models.ForeignKey(Discussion,related_name='comments',on_delete=models.CASCADE)
	content = models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=100)
	
	def __str__(self):
		return self.title