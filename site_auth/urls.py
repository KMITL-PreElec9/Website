from django.urls import path, include
from .views import UserProfileView, CheckProfileView
urlpatterns = [
    #path('base/',TemplateView.as_view(template_name='account/base.html')),
    path('', include('allauth.urls')),
    path('userprofile/', UserProfileView.as_view(), name='site_auth_userprofile'),
    path('profile/', CheckProfileView.as_view()),
]