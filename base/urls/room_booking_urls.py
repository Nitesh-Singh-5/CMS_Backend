from django.urls import path
from base.views import room_booking_views as views

urlpatterns = [
    path('', views.verificationProfile),
]
