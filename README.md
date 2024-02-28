# Chat App (Healthcare Domain)
This application is useful for doctors who can log in to their profile and record their patients with their data. There is also support for chat between doctors. So use it to your heart's content
## Endpoints 
What endpoints does this app have?
- "" This is the first one endpoints, and we have to register a doctor for it
- "profile/<int:doctor_id>/" After registration, we are taken to the profile window. Here you can see the information you provided in the registration, and just below the profile, we have a form to register your patients.
- "edit_doctor/<int:doctor_id>/" ,  "delete_doctor/<int:doctor_id>/" What are these two traps? In our profile, we have two buttons: delete profile and edit profile. And they redirect to these endpoints. There you can correct the data about yourself, or delete your profile altogether.
- <int:doctor_id> This is your unique identity. It is automatically assigned to you when you register. And it records you in the database
