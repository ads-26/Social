from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
	class Meta:
		model=Image
		fields=['title','img','description']
	"""
		widgets={
		'url':forms.HiddenInput,
		}
	
    
	def clean_url(self):
		url=self.cleaned_data['url']
		valid_extensions=['jpg','jpeg','png']
		#extension=url.rsplit('.',1).lower()
		extension=url.rsplit('.',1)
		if extension not in valid_extensions:
			raise forms.ValidationError('The given link does not give valid image extensions.')
		return url

	def save(self, force_insert=False,force_update=False,commit=True):    
		image = super(ImageCreateForm, self).save(commit=False)    
		#img_url = self.cleaned_data['url']    
		#img_name = '{}.{}'.format(slugify(image.title),img_url.rsplit('.', 1)[1].lower())
		img_name = '{}'.format(slugify(image.title))  
		response = request.open(image)    
		image.image.save(img_name,ContentFile(response.read()),save=False)    
		if commit:        
			image.save()    
			return image

	"""