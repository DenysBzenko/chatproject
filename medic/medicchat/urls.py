from django.urls import path
from .views import register_doctor, view_doctors, doctor_profile, chat_list, edit_doctor, delete_doctor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', register_doctor, name='register_doctor'),
    path('doctors/', view_doctors, name='view_doctors'),
    path('profile/<int:doctor_id>/', doctor_profile, name='doctor_profile'),
    path('chat/', chat_list, name='chat_list'),
    path('edit_doctor/<int:doctor_id>/', edit_doctor, name='edit_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
