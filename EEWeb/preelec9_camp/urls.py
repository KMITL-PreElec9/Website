from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import *
urlpatterns = [
    path('', CampIndexView.as_view()),
    path('63/statement/', CampStatementView.as_view())
] 