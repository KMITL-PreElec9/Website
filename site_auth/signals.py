from allauth.account.signals import user_logged_in, user_signed_up
from django.dispatch import receiver
from .models import *
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import Group,User

db = [EEData_63, EEData_64]

@receiver(post_save, sender = EEUserProfile)
def filled_userprofile(sender, instance, created, **kwargs):
    user_group = ['63_student', '64_student','62_student','61_student'] 
    user = User.objects.get(username = instance.user.username)
    user.groups.clear()
    g = Group.objects.get(name = 'guest')
    for i in range(len(db)):
        emails = instance.user.emailaddress_set.values()
        for user_email in emails:
            try: 
                    data = db[i].objects.get(email = user_email['email'])
                    g = Group.objects.get(name = user_group[i])
            except: pass
            try: 
                    data = db[i].objects.get(email2 = user_email['email'])
                    g = Group.objects.get(name = user_group[i])
            except: pass
    g.user_set.add(instance.user)

@receiver(user_signed_up)
def user_signed_up_signal_handler(request, user, **kwargs):
    user_email = user.email
    for i in range(len(db)):
        try: 
            try:
                data = db[i].objects.get(email = user_email)
            except: pass
            try:
                data = db[i].objects.get(email2 = user_email)
            except: pass
            data.used = True
            data.save()
            profile = EEUserProfile(
                name = data.name, surname = data.surname,
                student_id = data.student_id, 
                self_telephone_num = data.self_telephone_num,
                line_id = data.line_id, birth_date = data.birth_date, 
                nickname = data.nickname
            )
            
            profile.eng_name = str(user.frst_name).title()
            profile.eng_surname = str(user.last_name).title()
            profile.user = user
            profile.save(force_insert=True)
        except: pass
'''
@receiver(user_logged_in)
def user_signed_in_signal_handler(request, user, **kwargs):
    #If userprofile is not completed -> Redirect to edit profile page 
    
    #try: EEUserProfile.objects.get(user = user).exists()
    #except:
        print('I am working!')
        return redirect('/camp')
'''