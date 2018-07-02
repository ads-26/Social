from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True) 
	slug=models.SlugField(max_length=200,blank=True)
	#url=models.URLField()
	img=models.ImageField(upload_to='image/')
	description=models.TextField(blank=True)
	created=models.DateField(auto_now_add=True,db_index=True)


	def __str__(self):
		return self.title

	def save(self,*args,**kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
			super(Image,self).save(*args,**kwargs)
# Create your models here.