from django.urls import path
from authen.views import *

urlpatterns = [
    path('user_sigin_in_views/',UserSiginInViews.as_view()),
    path('user_information_views/',UserInformationViews.as_view()),
    path('user_logout_views/',UserLogoutViews.as_view()),
    path('user_create_views/',UserCreateViews.as_view()),
]