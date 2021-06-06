from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import UserProfileView
urlpatterns = [
    #path('base/',TemplateView.as_view(template_name='account/base.html')),
    path('', include('allauth.urls')),
    path('userprofile/', UserProfileView.as_view()),
    path('profile/', RedirectView.as_view(pattern_name ='home')),
]