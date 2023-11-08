from django.urls import path

from . import views

urlpatterns = [
    path("", views.greeting, name="greeting"),
    path("blog/<int:blog_id>", views.blog_view, name='blog'),
]
