from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from .forms import ImageCreateForm
from .models import Image


@login_required 
def image_create(request):	
	if request.method == 'POST':        
		form = ImageCreateForm(data=request.POST,files=request.FILES)        
		if form.is_valid():        
			cd = form.cleaned_data
			      
			new_item = form.save(commit=False)            
			new_item.user = request.user            
			new_item.save()         
			messages.success(request, 'Image added successfully')                
	else:
		form = ImageCreateForm(data=request.GET)

	return render(request,'image/img/create.html',{'section': 'images','form': form})
