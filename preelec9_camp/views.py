from django import forms
from django.db import models
from django.db.models.expressions import F
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from .decorators import *
from .models import Camp_Registered_64, Campdata_63, Campdata_64, Statement,Shirt
from django.contrib.auth.models import User
from .forms import RegisterForm_64, StatementForm_63,RegisterForm_63,Check_shirtForm
from site_auth.models import EEUserProfile,EEData_63,EEData_64
from django.utils import timezone
import qrcode
import qrcode.image.svg
from io import BytesIO

def campmenu(View):
    if View.request.user.groups.exists():
        group = View.request.user.groups.all()[0].name
    else: return False
    #กรณีน้อง
    if group == '64_student':
        try:
            db = View.request.user.campdata_64
            menu = [
                ['ตรวจสอบข้อมูล','64/viewdata/','ตรวจสอบและแก้ไขข้อมูลที่ลงทะเบียน','file', 'orange'],
                ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
                ['ใบขออนุญาตผู้ปกครอง','64/parent/', 'ดาวน์โหลด และพิมพ์ใบขออนุญาตผู้ปกครอง','book-open', 'yellow'],
                ['ยกเลิกการสมัคร','64/unregister/', 'ยกเลิกการสมัครเข้าค่าย','calendar-x', 'pink'],
            ]
        except Campdata_64.DoesNotExist:
            
            menu = [
                ['สมัครเข้าค่าย','64/register/','สมัครเข้าค่าย Pre-Electronics 9','calendar-plus','blue'],
               # ['ตรวจสอบตารางกิจกรรม','64/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบแบบ Real-Time','tachometer','orange'],
            ]
    #กรณีรุ่นเรา
    elif group in ['63_student', 'admin']:
        menu = [
                    ['สมัครเข้าค่าย','63/register/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue'],
                    ['ตรวจสอบข้อมูลรุ่นเรา','63/viewdata/', 'ตรวจสอบข้อมูลเพื่อนรุ่นเราที่ยืนยันเข้าค่าย','file', 'pink'],
                    ['บัญชีค่าย Pre-Elec9','63/statement/', 'ตรวจสอบบัญชีค่าย','book','yellow'],
                    ['ตรวจสอบตารางกิจกรรม','63/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
                ]
        try: 
            db = View.request.user.campdata_63
            if db.confirmed is True:
                menu = [
                        ['รายการสั่งซื้อ','63/register/','ตราวสอบรายการสั่งซื้อและหลักฐานการโอน','baseball', 'blue'],
                        ['ตรวจสอบข้อมูลน้อง','63/camp_listview/','ตรวจสอบข้อมูลน้องที่ลงทะเบียน','baseball', 'blue'],
                        ['ตรวจสอบข้อมูลรุ่นเรา','63/viewdata/', 'ตรวจสอบข้อมูลเพื่อนรุ่นเราที่ยืนยันเข้าค่าย','file', 'pink'],
                        ['บัญชีค่าย Pre-Elec9','63/statement/', 'ตรวจสอบบัญชีค่าย','book','yellow'],
                        ['สรุปข้อมูลต่างๆ','63/abstract/', 'สรุปรายการต่างๆ','book', 'red'],
                        ['ตรวจสอบตารางกิจกรรม','63/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
                        ['ยกเลิกการสมัคร','63/unregister/', 'ยกเลิกการสมัครเข้าค่าย','calendar-x', 'pink'],
                    ]
                if not db.check_shirt: menu.pop(0)
        except Campdata_63.DoesNotExist: pass

    else :
        menu = [
                    ['สั่งซื้อเสื้อค่าย','63/buyshirt/','สมัครเข้าทำค่าย Pre-Elec 9','baseball', 'blue']

                ]
    return menu


class CampIndexView(TemplateView):
    def dispatch(self, *args, **kwargs):
        try:
            if self.request.user.eeuserprofile.completed == False:
                return redirect('/accounts/userprofile/?next=/camp/')
        except: pass
        return super().dispatch(*args, **kwargs)
    template_name = "preelec9_camp/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampIndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'PreElec9-Camp'
        context['menu'] = campmenu(self)
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
        db = Statement
        if 'division' in self.request.GET.keys():
            getstr = str(self.request.GET['division'])
            if (getstr,getstr) in StatementForm_63.division_choices and getstr != 'All':
                data, total1, total2 = db.get_data_by_division(db,getstr)
                context['data'] = [[getstr, data, total1, total2]]
                context['total'] = total1 +total2
        else :
                context['data'] = []
                context['total'] = 0
                for tuple in StatementForm_63.division_choices:
                    data, total1, total2 = db.get_data_by_division(db,tuple[0])
                    context['data'].append([tuple[0], data, total1, total2])
                    context['total'] = context['total']+total1+total2
        
        context['form'] = StatementForm_63()
        return context

class RegisterView_64(FormView):
    template_name = "preelec9_camp/64/register.html"
    form_class = RegisterForm_64
    success_url = '/camp/'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(RegisterView_64, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Register'
        try:
            db = self.request.user.campdata_64.completed
            context['title'] = 'แก้ไขข้อมูลค่าย PreElec 9'
            context['button'] = 'บันทึกข้อมูล'
        except:
            context['title'] = 'สมัครค่าย PreElec 9'
            context['button'] = 'สมัครค่าย PreElec 9'
        return context
    def form_valid(self, form):
        model = form.save(commit = False)
        model.user = self.request.user
        model.save()
        Campdata_64.random_house(Campdata_64)
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        try: 
            data = Campdata_64.objects.filter(user = request.user).values()[0]
            self.initial = data
        except:
            pass
        return super().get(request,*args, **kwargs)
    def get_success_url(self, **kwargs) -> str:
        try:
            db = self.request.user.campdata_64.completed
            return self.request.GET['next']
        except:
            return 'confirm/'

class CampConfirmView(TemplateView):
    template_name = "preelec9_camp/64/confirm.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampConfirmView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Confirmation'
        context['data']=self.request.user.eeuserprofile
        return context
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        if 'confirm' in request.POST.keys():
            db = request.user.campdata_64.completed
            db = True
            db.save
        elif 'delete' in request.POST.keys():
            request.user.campdata_64.delete()
        else: pass 
        return redirect('/camp/')

class DataView_64(TemplateView):
    template_name = "preelec9_camp/64/viewdata.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['title_name'] = 'Viewdata'
        context['data'] = EEUserProfile.objects.get(user = self.request.user)
        context['campdata'] = Campdata_64.objects.get(user = self.request.user)
        context['regdata'] = Camp_Registered_64.objects.filter(campdata_64 = context['campdata'])
        return context

class CampUnregisterView(TemplateView):
    template_name = "preelec9_camp/64/unregister.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampUnregisterView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Unregister'
        return context
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self,request,*args, **kwargs):
        request.user.campdata_64.delete()
        Campdata_64.random_house(Campdata_64)
        return redirect('/camp/')

class CampParentView(TemplateView):
    template_name = "preelec9_camp/64/parent.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(['64_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(CampParentView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Parent_Form'
        context['data'] = self.request.user
        id = self.request.user.pk
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(self.request.get_host()+reverse('qrcode', kwargs={'pk':id}), image_factory=factory, box_size=15)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        context["title_name"] = 'ใบขออนุญาตผู้ปกครอง'
        return context

class CampListView_63(ListView):
    model = Campdata_64
    template_name = 'preelec9_camp/63/listview.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(CampListView_63, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'ข้อมูลน้อง'
        return context

class Viewdata_63(ListView):#ข้อมูลพี่

    model = Campdata_63
    template_name = 'preelec9_camp/63/viewdata.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_queryset(self):
        return super().get_queryset().filter(confirmed = True)
    def get_context_data(self,*args, **kwargs):
        context = super(Viewdata_63, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'ข้อมูลพี่'
        return context

class CampDetailView_63(DetailView):
    model = User
    template_name = 'preelec9_camp/63/detailview.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CampRegistrarView_63(TemplateView):
    template_name = 'preelec9_camp/63/registrar.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        user = User.objects.get(pk = kwargs['pk'])
        context = super(CampRegistrarView_63, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'ลงทะเบียนน้อง'
        context['regdata'] = Camp_Registered_64.objects.filter(campdata_64 = user.campdata_64)
        context['userdata'] = EEUserProfile.objects.get(user=user)
        context['allow_new'] = True
        for obj in context['regdata']:
            if obj.registered_on_2 == None:
                context['allow_new'] = False
                break
        return context
    def post(self, *args, **kwargs):
        if 'delete' in self.request.POST.keys():
            db = Camp_Registered_64.objects.get(pk=self.request.POST['regID'])
            db.delete()
        elif 'sign_out' in self.request.POST.keys():
            db = Camp_Registered_64.objects.get(pk=self.request.POST['regID'])
            db.registered_on_2 = timezone.now()
            db.registered_by_2 = str(self.request.user.eeuserprofile.nickname) + ' '+  str(self.request.user.eeuserprofile.name)
            db.save()
        elif 'sign_in' in self.request.POST.keys():
            cuser = Campdata_64.objects.get(pk = kwargs['pk'])
            ruser = self.request.user
            db = Camp_Registered_64(comment=self.request.POST['comment'])
            db.registered_on_1 = timezone.now()
            db.campdata_64 = cuser
            db.registered_by_1 = ruser
            db.save()
        else: pass
        return redirect('/camp/63/camp_register/'+str(kwargs['pk']))

class RegisterView_63(TemplateView):
    template_name = 'preelec9_camp/63/register.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, *args, **kwargs):
        if 'regis' in self.request.POST.keys():
            if hasattr(self.request.user, 'campdata_63'):
                db = self.request.user.campdata_63
                db.confirmed =True
            else: 
                db = Campdata_63(user = self.request.user, confirmed= True)
                if hasattr(self.request.user, 'shirt_set'):
                    self.request.user.shirt_set.all().delete()
            db.save()
            return redirect('/camp/')
        elif 'delete' in self.request.POST.keys():
            db = Shirt.objects.get(pk=self.request.POST['regID'])
            db.delete()
        elif 'upload' in self.request.POST.keys():
            form = Check_shirtForm(self.request.POST,self.request.FILES)
            if form.is_valid():
                model = form.save(commit=False)
                if hasattr(self.request.user, 'campdata_63'):
                    self.request.user.campdata_63.delete()
                model.user = self.request.user
                model.confirmed=True
                model.save()
        elif 'submit' in self.request.POST.keys():
            form = RegisterForm_63(self.request.POST)
            if form.is_valid():
                model = form.save(commit=False)
                model.user = self.request.user
                model.save()
        else: pass
        return redirect('/camp/63/register')   
    def get_context_data(self,*args, **kwargs):
        try:
            form_instance = self.request.user.campdata_63
        except: form_instance = None
        context = super(RegisterView_63, self).get_context_data(*args,**kwargs)
        context['shirt'] = Shirt.objects.filter(user=self.request.user)
        context['title_name'] = 'ลงทะเบียนพี่'
        context['form'] = RegisterForm_63
        context['form2'] = Check_shirtForm(instance=form_instance)
        check_year = self.request.user.groups.all()
        context['price'] = 100
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

class RegisterView_6x(TemplateView):
    template_name = 'preelec9_camp/63/register.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['61_student','62_student','guest']))
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


class CampUnregisterView_63(TemplateView):
    template_name = "preelec9_camp/64/unregister.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampUnregisterView_63, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Unregister'
        return context
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self,request,*args, **kwargs):
        db = request.user.campdata_63
        if db.check_shirt:
            db.confirmed = False
            db.save()
        else: db.delete()
        return redirect('/camp/')

class QRView(View):
    def get(self,request,*args, **kwargs):
        try: 
            if request.user.groups.all()[0].name == '64_student':
                return redirect('/camp/64/viewdata/')
            elif request.user.groups.all()[0].name == '63_student':
                return redirect('/camp/63/camp_register/'+str(kwargs['pk']))
            else: pass
        except:
            return redirect('/camp/')

class Abstract(TemplateView):
    template_name = "preelec9_camp/63/abstract/main.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(Abstract, self).get_context_data(*args,**kwargs)
        context['num_63'] =len(Campdata_63.objects.all())
        context['num_63_all'] =len(EEData_63.objects.all())
        context['num_64'] =len(Campdata_64.objects.all())
        context['num_64_all'] =len(EEData_64.objects.all())
        context['title_name'] = 'สรุปรวม'
        return context

class Allergy(ListView):
    model = EEUserProfile
    template_name = "preelec9_camp/63/abstract/allergy.html"
    context_object_name = 'allergy'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(Allergy, self).get_context_data(*args,**kwargs)
        return context
    def get_queryset(self):
        db = EEUserProfile.objects.exclude(completed=False)
        if 'form' in self.request.GET.keys():
            if self.request.GET['form'] == 'a':
                queryset  = db.exclude(allergic_foods='-').order_by('allergic_foods')
            elif self.request.GET['form'] == 'b':
                queryset  = db.exclude(allergic_meds='-').order_by('allergic_meds')
            elif self.request.GET['form'] == 'c':
                queryset  = db.exclude(congenital_disease='-').order_by('congenital_disease')
            else:
                queryset = db.exclude(allergic_foods='-',allergic_meds='-',congenital_disease='-').order_by('-student_id')
        else:
            queryset = db.exclude(allergic_foods='-',allergic_meds='-',congenital_disease='-').order_by('-student_id')
        return queryset

class CheckRegister(ListView):
    model = Campdata_64
    context_object_name = 'checkregister'
    template_name = "preelec9_camp/63/abstract/checkregister.html"
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    @method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(CheckRegister, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'เช็คการลงทะเบียน'
        return context
    def get_queryset(self):
        db = Campdata_64.objects.all()
        regis = []
        not_regis = []
        for obj in db :
            if obj.camp_registered_64_set.exists():
                for attr in obj.camp_registered_64_set.all():
                    if attr.registered_on_2 == None:
                        regis.append(obj)
                        if obj in not_regis:
                            not_regis.remove(obj)
                        break
                    else: 
                        if obj not in not_regis: not_regis.append(obj)            
            else: not_regis.append(obj)
        queryset = {
            'regis' : regis,
            'not_regis' : not_regis
        }
        return queryset    

class Checkshirt(ListView):
    model = Shirt
    template_name = "preelec9_camp/63/abstract/checkshirt.html"
   #@method_decorator(login_required)
    #@method_decorator(allowed_users(['63_student']))
    #@method_decorator(registered_only)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(Checkshirt, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'ข้อมูลพี่'
        return context
