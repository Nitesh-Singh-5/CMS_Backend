from django.urls import path
from base.views import room_views as views

urlpatterns = [

    path('', views.getRooms, name="Rooms"),

    path('create/', views.createRoom, name="Room-create"),
    path('upload/', views.uploadImage, name="image-upload"),

    path('<str:pk>/', views.getRoom, name="room"),

    path('update/<str:pk>/', views.updateRoom, name="room-update"),
    path('delete/<str:pk>/', views.deleteRoom, name="room-delete"),
]
