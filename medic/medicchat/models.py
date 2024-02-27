from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    specialty = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.patient.name} - {self.timestamp}'


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Doctor, related_name='chat_rooms')

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} - {self.timestamp}'
