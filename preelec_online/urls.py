from django.urls import path
from .views import *

urlpatterns = [
    path('', CampIndexView.as_view()),
    path('6x/shop/', Shop_6x.as_view()),
    path('6x/check_shop/',Checkshop.as_view()),
    path('64/regis/',Regis_64.as_view())
    
    ]
