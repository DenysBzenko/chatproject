# Chat App (Healthcare Domain)
This application is useful for doctors who can log in to their profile and record their patients with their data. There is also support for chat between doctors. So use it to your heart's content
# Getting Started
## Prerequisities
- Python 3.12 
- Django 5.0.2
## Clone repo 
- ```https://github.com/DenysBzenko/chatproject.git ```
- ```cd chatproject```
## Start the application
Start Django server (running on port 8000)
``` python manage.py runserver ```
## How to Use
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/8fa35dbe-ecc1-4d09-b3eb-76db3d851aec)
- When we clicked on the link. A registration window appears. Enter your information here. Your name, your age. Your profession in the field of medicine.
- For example 
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/f24aee4a-e0da-4a81-a269-6f4b3c120855)
- Click sing in
- Then you are redirected to your profile. We see http://127.0.0.1:8000/profile/13/ and the last digit indicates your personal ID. And here you can see all the information you have entered about yourself. That is, you have registered in the database, and it is now all yours.
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/c6b93f1a-183f-44c7-8c7a-92e9b72afe14)
- If your information is not accurate or you made a mistake and entered it incorrectly. There are two buttons. One for editing your profile, the other for deleting the profile (note that the profile is deleted permanently from the database and you will no longer be able to enter it, only create a new one)
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/f1e60c26-d849-4a04-8e40-e63ec1225159)
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/dd9ff86c-05f7-49f3-abe1-cd6d0efaf7b6)
- This is what these pages look like. 
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/981fe1a0-5712-416c-a5ac-aeed88afe237)
- ![image](https://github.com/DenysBzenko/chatproject/assets/119534908/53a3944c-9dd9-497f-b96b-84d68ef252e9)
- Next, you have the opportunity to enter your patient, enter their information (NAME, AGE, DISEASE). After that, confirm. And your patient is added to the database, and there is information about him/her and who is treating him/her
## Endpoints 
What endpoints does this app have?
- "" This is the first one endpoints, and we have to register a doctor for it
- "profile/<int:doctor_id>/" After registration, we are taken to the profile window. Here you can see the information you provided in the registration, and just below the profile, we have a form to register your patients.
- "edit_doctor/<int:doctor_id>/" ,  "delete_doctor/<int:doctor_id>/" What are these two traps? In our profile, we have two buttons: delete profile and edit profile. And they redirect to these endpoints. There you can correct the data about yourself, or delete your profile altogether.
- <int:doctor_id> This is your unique identity. It is automatically assigned to you when you register. And it records you in the database
