from django.contrib import admin
from django.urls import path, include
import form.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form.views.index, name="index"),
    path('detail/<int:detail_id>', form.views.detail, name="detail"),
    path('new/', form.views.new, name="new"),
    path('edit/<int:blog_id>', form.views.updateform, name="updateform"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
