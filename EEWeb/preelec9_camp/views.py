from django import forms
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Campdata_64, Statement
from .forms import RegisterForm_64

class CampIndexView(TemplateView):
    template_name = "preelec9_camp/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampIndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'PreElec9-Camp'
        return context

class CampStatementView(TemplateView):
    template_name = "preelec9_camp/63/statement.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self,*args, **kwargs):
        context = super(CampStatementView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Camp Statements'
        context['data'] = Statement.objects.all()
        return context
class RegisterView_64(FormView):
    template_name = "preelec9_camp/64/register.html"
    form_class = RegisterForm_64
    success_url = '/camp/'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def form_valid(self, form):
        model = form.save(commit = False)
        model.user = self.request.user
        model.save()
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        try: 
            data = Campdata_64.objects.filter(user = request.user).values()[0]
            self.initial = data
        except:
            pass
        return super().get(request,*args, **kwargs)
        