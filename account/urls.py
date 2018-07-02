from django.urls import path
from django.contrib.auth.views import login,logout,password_change,password_change_done,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from . import views
#app_name='account'

urlpatterns = [
    path('edit/',views.edit,name='edit'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('', views.dashboard,name='dashboard'),
    path('password-change/',password_change,name='password_change'),
    path('password-change/done/',password_change_done,name='password_change_done'),
    path('password-reset/',password_reset,name='password_reset'),
    path('password-reset/done/',password_reset_done,name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',password_reset_confirm,name='password_reset_confirm'),
    path('password-reset/complete/',password_reset_complete,name='password_reset_complete'),
    path('register/',views.register,name='register'),


]
