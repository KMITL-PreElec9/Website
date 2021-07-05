from django.shortcuts import render
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from .models import *
from .menu import campmenu
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from preelec9_camp.decorators import *
from .forms import *


class CampIndexView(TemplateView):
    def dispatch(self, *args, **kwargs):
        try:
            if self.request.user.eeuserprofile.completed == False:
                return redirect('/accounts/userprofile/?next=/camp/')
        except: pass
        return super().dispatch(*args, **kwargs)
    template_name = "preelec_online/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampIndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'PreElec Online'
        context['menu'] = campmenu(self)
        return context

class Shop_6x(TemplateView):
    template_name = 'preelec_online/6x/shop.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student','61_student','62_student','guest']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)   
    def get_context_data(self,*args, **kwargs):
        context = super(Shop_6x, self).get_context_data(*args,**kwargs)
        if hasattr(self.request.user,'camp_online_6x'):
            context['shop'] = Shop.objects.filter(camp_online_6x=self.request.user.camp_online_6x)
        context['title_name'] = 'สั่งซื้อเสื้อค่าย'
        context['forms'] = [Powerbank_form(),Bag_form()]
        return context
    def post(self,request,*args, **kwargs):
        if Bag_form.Meta.form_name in self.request.POST.keys():
            form = Bag_form(self.request.POST)
        elif Powerbank_form.Meta.form_name in self.request.POST.keys():
            form = Powerbank_form(self.request.POST)
        try: 
            if form.is_valid: form.save(self.request.user)
        except: pass
        return render(request, self.template_name,self.get_context_data())
