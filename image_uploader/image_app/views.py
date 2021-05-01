from django.shortcuts import render
from .forms import ImageForm
from .models import Image
import os
from image_uploader.settings import BASE_DIR


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        print(form)
        print(type(form))
        if form.is_valid():
            form.save()
    image_form = ImageForm()
    all_images = Image.objects.all()
    return render(request, "multi_image_template/home.html",
                  {"image_form": image_form,
                   "all_images": all_images})


def delete_image(request, iid):
    image_to_delete = Image.objects.filter(id=iid).first()
    if image_to_delete:
        pass
        image_to_delete.delete()
        cwd = os.getcwd()
        # print("\nCurrent Working Directory----", cwd, "\n")
        img_path = cwd + str(image_to_delete.photo.url)
        print("IMAGE_PATH--->", img_path)
        os.remove(img_path)
    image_form = ImageForm()
    all_images = Image.objects.all()
    return render(request, "multi_image_template/home.html",
                  {"image_form": image_form,
                   "all_images": all_images})
