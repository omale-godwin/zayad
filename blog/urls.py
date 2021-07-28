from . import views
from django.urls import path

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('<int:blog_id>', views.blogdetail, name='blogdetail'),
    # path("service", views.service, name="service")
]

