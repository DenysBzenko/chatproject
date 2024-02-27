from django.urls import path
from .views import register_doctor

urlpatterns = [
    path('', register_doctor, name='register_doctor'),

]
