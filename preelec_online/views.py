from preelec9_camp.views import RegisterView_64
from django.db.models import query
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView, FormView
from .models import *
from .menu import campmenu
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from preelec9_camp.decorators import *
from .forms import *
from preelec9_camp.models import Statement
from django.utils import timezone

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
        context['title_name'] = 'ยืนยันและชำระเงิน'
        db = Camp_online_6x.objects.get(user = self.request.user)
        context['confirmed'] = db.confirmed
        context['form'] = ShopCheckoutForm(instance= db)
        return context
    def post(self, request, *args, **kwargs):
        db = Camp_online_6x.objects.get(user = self.request.user)
        form = ShopCheckoutForm(self.request.POST,self.request.FILES, instance= db)
        print(form.is_valid())
        if form.is_valid():
            model = form.save(commit = False)
            shop_list = self.request.user.camp_online_6x.shop_set.values()
            total = 0
            for obj in shop_list:
                total += obj['quantity']*obj['price']
            model.price = total
            model.save()
        return HttpResponseRedirect(self.request.path_info)

class OrderListView_6x(ListView):
    model = Camp_online_6x
    template_name = "preelec_online/6x/orderlist.html"
    context_object_name = 'order'
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('/camp/')
        return super().dispatch(*args, **kwargs) 
    def get_context_data(self,*args, **kwargs):
        context = super(OrderListView_6x, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'รายการสั่งซื้อ'
        return context
    def get_queryset(self):
        queryset = self.model.objects.filter(completed=True).order_by('confirmed')
        return queryset

class OrderDetailView_6x(TemplateView):
    template_name = "preelec_online/6x/orderdetail.html"
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('/camp/')
        return super().dispatch(*args, **kwargs) 
    def get_context_data(self,pk, **kwargs):
        context =  super().get_context_data(**kwargs)
        db = Camp_online_6x.objects.get(pk = pk)
        context['title_name'] = 'ตรวจสอบและยืนยันการสั่งซื้อ'
        context['data'] = db.user.eeuserprofile
        context['img'] = db.check_shop
        context['confirmed'] = db.confirmed
        context['shop_list'] = db.shop_set.all().values()
        return context
    def post(self, *args, **kwargs):
        if 'confirm' in self.request.POST.keys():
            db = Camp_online_6x.objects.get(pk = kwargs['pk'])
            p = db.user.eeuserprofile
            display_name = 'ค่าสินค้าของ {} {} {}'.format(p.gender, p.name, p.surname)
            db.confirmed = True
            db.save()
            statement = Statement(
                division = 'Art', mode = 'รายรับ', item_name = display_name,
                transaction_date = timezone.now(), price = db.price,
                quantity = 1, remarks='เพิ่มโดยระบบ (อัตโนมัติ)'
                )
            statement.save()
        return HttpResponseRedirect(self.request.path_info)

class RegisterView(TemplateView):
    template_name = 'preelec_online/64/regis.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs) 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = "ลงทะเบียน"
        return context
    def post(self,*args, **kwargs):
        if 'regis' in self.request.POST.keys():
            db = Camp_online_64(user = self.request.user)
            db.save()
        return redirect('/camp/')

class QrConfirmView(RegisterView):
    template_name = 'preelec_online/64/qrconfirm.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = "ลงทะเบียน"
        return context
    def post(self,*args, **kwargs):
        if 'regis' in self.request.POST.keys():
            db = self.request.user.camp_online_64
            db.confirmed = True
            db.save()
        return redirect('/camp/')
class CheckRegisterView_64(ListView):
    model = Camp_online_64
    template_name = "preelec_online/64/datalist.html"
    context_object_name = 'data'
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('/camp/')
        return super().dispatch(*args, **kwargs) 
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title_name'] = 'น้องที่ลงทะเบียน'
        return context
    def get_queryset(self):
        queryset = self.model.objects.filter(confirmed=True).order_by('confirmed')
        return queryset