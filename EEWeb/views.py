from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self,*args, **kwargs):
        context = super(IndexView, self).get_context_data(*args,**kwargs)
        context['camp']=True
        if self.request.user.is_authenticated:
            if self.request.user.groups.all()[0].name == '64_student':
                context['camp'] = True
            else:
                context['camp'] = False
        context['title_name'] = 'EE KMITL'
        return context