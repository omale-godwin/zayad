from . import views
from django.urls import path

urlpatterns = [
    path('event', views.event, name='event'),
    path('<int:event_id>', views.eventdetail, name='eventdetail'),
    # path("service", views.service, name="service")
]

