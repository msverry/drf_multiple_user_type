from django.urls import path
from rest_framework.authtoken import views as auth_views
from user import views as user_views


urlpatterns = [
    path('login/', auth_views.obtain_auth_token),
    path('customer/', user_views.CustomerInfo.as_view()),
    path('employee/', user_views.EmployeeInfo.as_view()),
]
