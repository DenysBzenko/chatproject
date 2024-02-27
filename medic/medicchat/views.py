from django.shortcuts import render
from .models import Doctor
from django.shortcuts import redirect

def register_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        specialty = request.POST.get('specialty')
        Doctor.objects.create(name=name, age=age, specialty=specialty)
        return redirect('profile')
    else:
        return render(request, 'registration.html')

def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'view_doctors.html', {'doctors': doctors})

def doctor_profile(request):
    # Отримання останнього зареєстрованого лікаря
    latest_doctor = Doctor.objects.latest('id')
    return render(request, 'profile.html', {'doctor': latest_doctor})
