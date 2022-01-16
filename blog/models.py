from django.db import models

# Create your models here.

class Blog(models.Model):
	model_title = models.CharField(max_length=300)
	model_date = models.DateTimeField()
	model_text = models.TextField()
	model_image = models.ImageField(upload_to='model_images/', default='')
