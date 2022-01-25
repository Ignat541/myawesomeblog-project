from django.db import models

# Create your models here.

class Blog(models.Model):
	model_title = models.CharField(max_length=300)
	model_date = models.DateTimeField()
	model_text = models.TextField()
<<<<<<< HEAD
	model_image = models.ImageField(upload_to='event_images/', default='')


	def summary(self):
		return self.model_text[:70]
=======
	model_image = models.ImageField(upload_to='model_images/', default='')
>>>>>>> c7bce7816e4a2acac17d70bd3d4b1aea577abcec
