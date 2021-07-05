from django.urls import path
from .views import *

urlpatterns = [
    path('', CampIndexView.as_view()),
    path('6x/shop/', Shop_6x.as_view()),
    path('6x/shop/checkout/', ShopCheckoutView.as_view())
    ]
