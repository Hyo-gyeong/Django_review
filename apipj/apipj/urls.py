from django.contrib import admin
from django.urls import path
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.views.home, name='home'),
    path('detail/<int:blog_id>', api.views.detail, name='detail'),
    path('new/', api.views.new, name='new'),
    path('edit/<int:blog_id>', api.views.edit, name='edit'),
]
