from django.views.generic import TemplateView
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(IndexView, self).get_context_data(*args,**kwargs)
        context['title_name'] = 'EE KMITL'
        return context