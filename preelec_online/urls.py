from django.urls import path
from .views import *

urlpatterns = [
    path('', CampIndexView.as_view()),
    path('6x/shop/', Shop_6x.as_view()),
    path('6x/shop/checkout/', ShopCheckoutView.as_view()),
    path('6x/orderlist/', OrderListView_6x.as_view()),
    path('6x/orderdetail/<int:pk>/', OrderDetailView_6x.as_view()),
    path('64/register/', RegisterView.as_view()),
    path('64/datalist/', CheckRegisterView_64.as_view()),
    path('qrcode/confirm', QrConfirmView.as_view())
    ]
