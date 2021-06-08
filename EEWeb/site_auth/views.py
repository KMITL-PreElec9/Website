from django.db.models.query import InstanceCheckMeta
from django.views.generic import View
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import EEUserProfile
from .forms import ProfileForm

class CheckProfileView(View):
    def get(self,request,*args, **kwargs):
        try: 
            db = EEUserProfile.objects.get(user = request.user, completed = True)
            return redirect('home')
        except:
            return redirect('site_auth_userprofile')
        

class UserProfileView(FormView):
    template_name = 'profile/userprofile.html'
    form_class = ProfileForm
    success_url = '/accounts/userprofile'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(UserProfileView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'User Profile'
        context['data'] = EEUserProfile.objects.get(user = self.request.user)
        try:
            context['back_url'] = self.request.GET['next']
        except: context['back_url'] = '/'
        return context
    def get(self, request, *args, **kwargs):
        try: 
            EEUserProfile.objects.filter(user = request.user).values()[0]
        except:
            db = EEUserProfile(user = request.user)
            db.save()
        self.initial = EEUserProfile.objects.filter(user = request.user).values()[0]
        return super().get(request,*args, **kwargs)
    def form_valid(self, form):
        model = form.save(commit = False)
        model.user = self.request.user
        model.completed = True
        model.save()
        return super().form_valid(form)




