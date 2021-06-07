from django.views.generic import TemplateView
class CampIndexView(TemplateView):
    template_name = "preelec9_camp/index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CampIndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'PreElec9-Camp'
        return context