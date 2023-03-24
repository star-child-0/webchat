from django.urls import path
from chat import views


app_name = 'chat'
urlpatterns = [
	path("rooms/", views.rooms, name="rooms"),
	path("rooms/<str:room_name>/", views.room, name="room"),
    
	path("chat/", views.chat, name="chat"),
	path("ajax_send_message", views.ajax_send_message, name="ajax_send_message"),
]
