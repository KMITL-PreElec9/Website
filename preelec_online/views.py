from django.shortcuts import render
from .serializers import UserSerializer
from django.http import Http404, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView, FormView
from .models import *
from .menu import campmenu
from site_auth.models import EEUserProfile,EEData_63,EEData_64
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
        try:
            if self.request.user.camp_online_6x.completed == True:
                return redirect('checkout/')
        except:pass
        return super().dispatch(*args, **kwargs)   
    def get_context_data(self,*args, **kwargs):
        context = super(Shop_6x, self).get_context_data(*args,**kwargs)
        context['total'] = 0
        if hasattr(self.request.user,'camp_online_6x'):
            context['shop'] = Shop.objects.all().filter(camp_online_6x = self.request.user.camp_online_6x)
            for obj in context['shop'].values():
                context['total'] += obj['quantity']*obj['price']
        context['title_name'] = 'สั่งซื้อสินค้า'
        context['forms'] = [Powerbank_form(),Bag_form()]
        return context
    def post(self,request,*args, **kwargs):
        if Bag_form.Meta.form_name in self.request.POST.keys():
            form = Bag_form(self.request.POST)
        elif Powerbank_form.Meta.form_name in self.request.POST.keys():
            form = Powerbank_form(self.request.POST)
        elif 'delete' in self.request.POST.keys():
            db = Shop.objects.get(pk = self.request.POST['regID'])
            db.delete()
            if len(Shop.objects.all().filter(camp_online_6x = self.request.user.camp_online_6x)) == 0:
                self.request.user.camp_online_6x.delete()
        try: 
            if form.is_valid: form.save(self.request.user)
        except: pass
        return redirect('/camp/6x/shop/')

class ShopCheckoutView(TemplateView):
    template_name='preelec_online/6x/checkout.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student','61_student','62_student','guest']))
    def dispatch(self, *args, **kwargs):
        if not hasattr(self.request.user, 'camp_online_6x'):
            return redirect('/camp/')
        return super().dispatch(*args, **kwargs) 
    def get_context_data(self,*args, **kwargs):
        context = super(ShopCheckoutView, self).get_context_data(*args,**kwargs)
        context['total'] = 0
        if hasattr(self.request.user,'camp_online_6x'):
            context['shop'] = Shop.objects.all().filter(camp_online_6x = self.request.user.camp_online_6x)
            for obj in context['shop'].values():
                context['total'] += obj['quantity']*obj['price']
        context['title_name'] = 'สั่งซื้อสินค้า'
        context['forms'] = [Powerbank_form(),Bag_form()]
        context['title_name'] = 'ยืนยันและชำระเงิน'
        db = Camp_online_6x.objects.get(user = self.request.user)
        context['confirmed'] = db.confirmed
        context['form'] = ShopCheckoutForm(instance= db)
        context['img'] = db.check_shop
        return context
    def post(self, request, *args, **kwargs):
        db = Camp_online_6x.objects.get(user = self.request.user)
        form = ShopCheckoutForm(self.request.POST,self.request.FILES, instance= db)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(self.request.path_info)
