from django.urls import path
from .views import register_doctor, view_doctors , doctor_profile, chat_list, edit_doctor,delete_doctor


urlpatterns = [
    path('', register_doctor, name='register_doctor'),
    path('doctors/', view_doctors, name='view_doctors'),
    path('profile/', doctor_profile, name='profile'),
    path('chat/', chat_list, name='chat_list'),
    path('edit_doctor/<int:doctor_id>/', edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
]
