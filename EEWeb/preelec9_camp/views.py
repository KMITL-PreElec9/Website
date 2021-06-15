from django import forms
from django.db import models
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import *
from .models import Camp_Registered_64, Campdata_64, Statement
from django.contrib.auth.models import User
from .forms import RegisterForm_64, StatementForm_63
from site_auth.models import EEUserProfile

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
                ['ตรวจสอบข้อมูลน้อง','63/camp_listview/','ตรวจสอบข้อมูลน้องที่ลงทะเบียน','baseball', 'blue'],
                ['ตรวจสอบข้อมูลรุ่นเรา','63/viewdata/', 'ตรวจสอบข้อมูลเพื่อนรุ่นเราที่ยืนยันเข้าค่าย','file', 'pink'],
                ['บัญชีค่าย Pre-Elec9','63/statement/', 'ตรวจสอบบัญชีค่าย','book','yellow'],
                ['ตรวจสอบตารางกิจกรรม','63/table/', 'ตรวจสอบตารางกิจกรรมและจุดนัดพบ','tachometer', 'red'],
            ]
    else: return False
    return menu


class CampIndexView(TemplateView):
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
        if 'division' in self.request.GET.keys():
            getstr = str(self.request.GET['division'])
            db = Statement
            if (getstr,getstr) in StatementForm_63.division_choices and getstr != 'All':
                data, total1, total2 = db.get_data_by_division(db,getstr)
                context['data'] = [[getstr, data, total1, total2]]
                context['total'] = total1 +total2
            elif getstr == 'All':
                context['data'] = []
                context['total'] = 0
                for tuple in StatementForm_63.division_choices:
                    data, total1, total2 = db.get_data_by_division(db,tuple[0])
                    context['data'].append([tuple[0], data, total1, total2])
                    context['total'] = context['total']+total1+total2
            else: pass   
        else:
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
        return context
class CampListView_63(ListView):
    model = Campdata_64
    template_name = 'preelec9_camp/63/listview.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_context_data(self,*args, **kwargs):
        context = super(CampListView_63, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'ข้อมูลน้อง'
        return context
class CampDetailView_63(DetailView):
    model = User
    template_name = 'preelec9_camp/63/detailview.html'
    @method_decorator(login_required)
    @method_decorator(allowed_users(['63_student']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
