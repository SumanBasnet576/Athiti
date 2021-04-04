from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import (
    UserRegistration,
    UserLogin,


)

router = DefaultRouter()
router.register('login', UserLogin, base_name="login"),


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('', include(router.urls)),

]
