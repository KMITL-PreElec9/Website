from django.views.generic import TemplateView
class RegisterView(TemplateView):
    template_name = "site_auth/index.html"
