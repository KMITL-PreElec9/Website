from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import *
urlpatterns = [
    path('', CampIndexView.as_view()),
    path('63/statement/', CampStatementView.as_view()),
    path('64/register/', RegisterView_64.as_view()),
    path('64/register/confirm/', CampConfirmView.as_view()),
    path('64/unregister/', CampUnregisterView.as_view()),
    path('64/viewdata/', DataView_64.as_view()),
    path('64/parent/', CampParentView.as_view())
] 
