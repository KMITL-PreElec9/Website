from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    path('', CampIndexView.as_view()),
    path('63/statement/', CampStatementView.as_view()),
    path('63/register/', RegisterView_63.as_view()),
    path('63/camp_listview/', CampListView_63.as_view()),
    path('63/camp_listview/<int:pk>/', CampDetailView_63.as_view()),
    path('63/camp_register/<int:pk>/', CampRegistrarView_63.as_view()),
    path('63/unregister/', CampUnregisterView_63.as_view()),
    path('63/viewdata/',viewdata_63.as_view()),
    path('64/register/', RegisterView_64.as_view()),
    path('64/register/confirm/', CampConfirmView.as_view()),
    path('64/unregister/', CampUnregisterView.as_view()),
    path('64/viewdata/', DataView_64.as_view()),
    path('64/parent/', CampParentView.as_view()),
    path('qrcode/<int:pk>/', QRView.as_view(), name='qrcode')

]
