from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('room/<int:pk>', views.room, name='room'),
    path('create-room/', views.create_room, name='create_room'),
    path('update-room/<int:pk>', views.update_room, name='update_room'),
    path('delete-room/<int:pk>', views.delete_room, name='delete_room'),
]
