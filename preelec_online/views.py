from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from preelec9_camp.decorators import *

def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        try:
            db = View.request.user.camp_online_64
            menu = [
                ['ตรวจสอบข้อมูล','64/viewdata/','ตรวจสอบและแก้ไขข้อมูลที่ลงทะเบียน','file', 'orange'],
                ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
                ['ใบขออนุญาตผู้ปกครอง','64/parent/', 'ดาวน์โหลด และพิมพ์ใบขออนุญาตผู้ปกครอง','book-open', 'yellow'],
                ['ยกเลิกการสมัคร','64/unregister/', 'ยกเลิกการสมัครเข้าค่าย','calendar-x', 'pink'],
            ]
        except camp_online_64.DoesNotExist:
            
            menu = [
                ['สมัครเข้าค่าย','64/register/','สมัครเข้าค่าย Pre-Electronics 9','calendar-plus','blue'],
               # ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','orange'],
            ]
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin']:
        menu = [
                    ['สั่งซื้อสินค้า','6x/shop/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue']
                    
                ]
        try: 
            db = View.request.user.camp_online_6x
            if db.confirmed is True:
                menu = [
                        ['รายการสั่งซื้อ','63/register/','ตราวสอบรายการสั่งซื้อและหลักฐานการโอน','baseball', 'blue'],
                        ['ตรวจสอบข้อมูลรุ่นเรา','63/viewdata/', 'ตรวจสอบข้อมูลเพื่อนรุ่นเราที่ยืนยันเข้าค่าย','file', 'pink'],
                        ['บัญชีค่าย Pre-Elec9','63/statement/', 'ตรวจสอบบัญชีค่าย','book','yellow'],
                        ['ยกเลิกการสมัคร','63/unregister/', 'ยกเลิกการสมัครเข้าค่าย','calendar-x', 'pink'],
                    ]
                if not db.check_shirt: menu.pop(0)
        except camp_online_6x.DoesNotExist: pass

    else :
        menu = [
                    ['สั่งซื้อสินค้า','6x/shop/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue']

                ]
    return menu

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
    template_name = 'preelec_online/63/shop.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student','61_student','62_student','guest']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, *args, **kwargs):
        if 'delete' in self.request.POST.keys():
            db = Shirt.objects.get(pk=self.request.POST['regID'])
            db.delete()
        elif 'upload' in self.request.POST.keys():
            form = Check_shirtForm(self.request.POST,self.request.FILES)
            if form.is_valid():
                model = form.save(commit=False)
                if hasattr(self.request.user, 'campdata_6x'):
                    self.request.user.campdata_6x.delete()
                model.user = self.request.user
                model.save()
        elif 'submit' in self.request.POST.keys():
            form = RegisterForm_63(self.request.POST)
            if form.is_valid():
                model = form.save(commit=False)
                model.user = self.request.user
                model.save()
        else: pass
        return redirect('/camp/63/buyshirt/')   
    def get_context_data(self,*args, **kwargs):
        try:
            form_instance = self.request.user.campdata_63
        except: form_instance = None
        context = super(RegisterView_6x, self).get_context_data(*args,**kwargs)
        context['shirt'] = Shirt.objects.filter(user=self.request.user)
        context['title_name'] = 'สั่งซื้อเสื้อค่าย'
        context['form'] = RegisterForm_63
        context['form2'] = Check_shirtForm(instance=form_instance)
        context['year'] = True
        check_year = self.request.user.groups.all()
        if check_year[0] == '62_student':
            context['price'] = 200
        elif check_year[0] == '61_student':
            context['price'] = 300
        else:
            context['price'] = 300
        total = 0
        for obj in context['shirt'].values():
            total += int(obj["quantity_shirt"]) * context['price']
        context['total'] = total
        try:
            query = Campdata_63.objects.get(user=self.request.user)
            context['confirmed'] = query.confirmed
            context['img_obj']= query.check_shirt
        except:
            pass

        return context
