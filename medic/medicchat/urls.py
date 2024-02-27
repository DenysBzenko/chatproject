from django.urls import path
from .views import register_doctor, view_doctors , doctor_profile

urlpatterns = [
    path('', register_doctor, name='register_doctor'),
    path('doctors/', view_doctors, name='view_doctors'),
    path('profile/', doctor_profile, name='profile'),
]
