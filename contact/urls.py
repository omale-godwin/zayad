from . import views
from django.urls import path

urlpatterns = [
    path('contact', views.contact, name='contact'),
    # path('causesdetail', views.causesdetail, name='causesdetail'),

]

