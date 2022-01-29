from django.db import models

# Create your models here.

class Blog(models.Model):
	model_title = models.CharField(max_length=300)
	model_date = models.DateTimeField()
	model_text = models.TextField()

	model_image = models.ImageField(upload_to='event_images/', default='')


	def summary(self):
		return self.model_text[:70]

	def __str__(self):
		return self.model_title

