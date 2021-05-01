from django.shortcuts import render
# from .forms import ImageForm
import os
from image_uploader.settings import BASE_DIR

from image_uploader.settings import BASE_DIR
from image_app.models import Image

print(BASE_DIR)

image_to_delete = Image.objects.filter(id=35).first()

print(image_to_delete)

a = "D:\\django_sample_projects\\image_uploader\\media"
