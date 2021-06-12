from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Statement
class CampIndexView(TemplateView):
    template_name = "preelec9_camp/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampIndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'PreElec9-Camp'
        return context
class CampStatementView(TemplateView):
    template_name = "preelec9_camp/63/statement.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self,*args, **kwargs):
        context = super(CampStatementView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'Camp Statements'
        context['data'] = Statement.objects.all()
        return context