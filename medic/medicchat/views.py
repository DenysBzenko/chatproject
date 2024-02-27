from django.shortcuts import render
from .models import Doctor ,ChatRoom
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

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
    latest_doctor = Doctor.objects.latest('id')
    return render(request, 'profile.html', {'doctor': latest_doctor})

def chat_list(request):
    chats = ChatRoom.objects.all()
    return render(request, 'chat_list.html', {'chats': chats})

def chat_room(request, chat_id):
    chat = ChatRoom.objects.get(id=chat_id)
    return render(request, 'chat_room.html', {'chat': chat})

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.age = request.POST.get('age')
        doctor.specialty = request.POST.get('specialty')
        doctor.save()
        return redirect('profile')
    else:
        return render(request, 'edit_profile.html', {'doctor': doctor})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            doctor.delete()
            return redirect(reverse('register_doctor'))
    return render(request, 'delete_profile.html', {'doctor': doctor})

