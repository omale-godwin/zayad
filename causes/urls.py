from . import views
from django.urls import path

urlpatterns = [
    path('causes', views.causes, name='causes'),
    path('causesdetail', views.causesdetail, name='causesdetail'),
    # path("service", views.service, name="service")
]