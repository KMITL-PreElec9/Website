from django.urls import path
from .views import UserDetail
urlpatterns = [
    path('api/user', UserDetail.as_view())
]
