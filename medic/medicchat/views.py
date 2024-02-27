from django.shortcuts import render
from .models import Doctor
from django.http import  HttpResponse

def register_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        specialty = request.POST.get('specialty')
        Doctor.objects.create(name=name, age=age, specialty=specialty)
        return HttpResponse("")
    else:
        return render(request, 'registration.html')

