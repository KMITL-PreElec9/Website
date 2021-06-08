from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .models import EEUserProfile
from django.shortcuts import redirect

'''
@receiver(user_logged_in)
def user_signed_in_signal_handler(request, user, **kwargs):
    #If userprofile is not completed -> Redirect to edit profile page 
    
    #try: EEUserProfile.objects.get(user = user).exists()
    #except:
        print('I am working!')
        return redirect('/camp')
'''