from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from image_app.views import home, delete_image
import multi_image.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    # path('delete/<int:iid>', delete_image, name='delete_image'),
    path('multi/', multi_image.views.home, name='multi_home'),
    path('multi/delete/<int:iid>', multi_image.views.delete_image, name='multi_delete_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
