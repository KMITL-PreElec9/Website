from django.urls import path, include
from django.utils.translation import templatize
from .views import RegisterView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('base/',TemplateView.as_view(template_name='account/base.html')),
    path('', include('allauth.urls')),

]