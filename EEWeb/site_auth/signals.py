from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .models import EEUserProfile
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import Group,User

@receiver(post_save, sender = EEUserProfile)
def filled_userprofile(sender, instance, created, **kwargs):
    teststr = str(instance.student_id)
    checkstr = str(instance.user.email)
    user = User.objects.get(username = instance.user.username)
    user.groups.clear()

    if instance.completed == True and teststr in checkstr:
        if teststr[:2] == '62':
            g = Group.objects.get(name = '62_student')
        elif teststr[:2] == '63':
            g = Group.objects.get(name = '63_student')
        elif teststr[:2] == '64':
            g = Group.objects.get(name = '64_student')
        else:
            g = Group.objects.get(name = 'guest')
        g.user_set.add(instance.user)
'''
@receiver(user_logged_in)
def user_signed_in_signal_handler(request, user, **kwargs):
    #If userprofile is not completed -> Redirect to edit profile page 
    
    #try: EEUserProfile.objects.get(user = user).exists()
    #except:
        print('I am working!')
        return redirect('/camp')
'''