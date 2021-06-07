from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import CampIndexView
urlpatterns = [
    path('', CampIndexView.as_view())
] 