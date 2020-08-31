from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('<int:b_id>', blogapp.views.detail, name = 'detail'),
    path('update/<int:u_id>', blogapp.views.update, name = 'update'),
    path('<int:posts_id>/comment/create', blogapp.views.comment_create, name="comment_create"),
    path('search', blogapp.views.searchyy, name='searchzz'),
    path('create/', blogapp.views.create, name="create"),
]