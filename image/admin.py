from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
	list_display=['title','slug','img','created']
	list_filter=['created']


admin.site.register(Image,ImageAdmin)

# Register your models here.
