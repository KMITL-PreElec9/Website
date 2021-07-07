from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.http.response import HttpResponseRedirect
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
        data = EEUserProfile.objects.get(user = self.request.user)
        context['title_name'] = 'User Profile'
        context['data'] = data
        try:
            context['back_url'] = self.request.GET['next']
        except: context['back_url'] = '/'
        if 'edit' in self.request.GET.keys():
            context['completed'] = not bool(int(self.request.GET['edit']))
        else:
            context['completed'] = data.completed
        if 'message' in self.request.GET.keys():
            message = {
                'shop' : 'โปรดกดบันทึกข้อมูลเพื่อทำการชำระเงินต่อไป'
            }
            context['message'] = message[str(self.request.GET['message'])]
        return context
    def get(self, request, *args, **kwargs):
        try: 
            EEUserProfile.objects.filter(user = request.user).values()[0]
        except:
            db = EEUserProfile(user = request.user)
            db.save()
        self.initial = EEUserProfile.objects.filter(user = request.user).values()[0]
        return super().get(request,*args, **kwargs)
    '''
    def post(self,*args, **kwargs):
        form = ProfileForm(self.request.POST)
        print(form.is_valid())
        print(self.request.POST)
        return HttpResponseRedirect(self.request.path_info)
    '''
    def form_valid(self, form):
        model = form.save(commit = False)
        model.user = self.request.user
        model.completed = True
        model.save()
        return super().form_valid(form)
    def get_success_url(self, **kwargs) -> str:
        if 'next' in self.request.GET.keys():
            url = self.request.GET['next']
        else:
            url = '/'
        return url

        