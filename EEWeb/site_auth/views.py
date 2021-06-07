from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import EEUserProfile
from .forms import ProfileForm
class RegisterView(TemplateView):
    template_name = "site_auth/index.html"
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
        return context
    def get(self, request, *args, **kwargs):
        try: instance = EEUserProfile.objects.filter(user = request.user).values()[0]
        except:
            db = EEUserProfile(user = request.user)
            db.save()
        self.initial = EEUserProfile.objects.filter(user = request.user).values()[0]
        return super().get(request,*args, **kwargs)
    def form_valid(self, form):
        cd = form.cleaned_data
        db = EEUserProfile.objects.get(user = self.request.user)
        db.gender = cd['gender']
        db.name = cd['name']
        db.surname = cd['surname']
        db.nickname = cd['nickname']
        db.student_id = cd['student_id']
        db.birth_date = cd['birth_date']
        db.address = cd['address']
        db.self_telephone_num = cd['self_telephone_num']
        db.line_id = cd['line_id']
        db.facebook = cd['facebook']
        db.instagram = cd['instagram']
        db.completed = True
        db.save()
        return super().form_valid(form)




