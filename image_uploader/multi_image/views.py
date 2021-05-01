from django.shortcuts import render
from .models import MultiImage
import os


def home(request):
    if request.method == "POST":
        user_image_list = request.FILES.getlist('image')
        for image in user_image_list:
            MultiImage.objects.create(photo=image)

    all_images = MultiImage.objects.all()
    return render(request, "multi_image_template/home.html",
                  {"all_images": all_images})


def delete_image(request, iid):
    image_to_delete = MultiImage.objects.filter(id=iid).first()
    if image_to_delete:
        pass
        image_to_delete.delete()
        cwd = os.getcwd()
        # print("\nCurrent Working Directory----", cwd, "\n")
        img_path = cwd + str(image_to_delete.photo.url)
        print("IMAGE_PATH--->", img_path)
        os.remove(img_path)
    all_images = MultiImage.objects.all()
    return render(request, "multi_image_template/home.html",
                  {"all_images": all_images})
