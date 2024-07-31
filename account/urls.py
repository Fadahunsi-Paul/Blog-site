from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from account import views as user_views
app_name = "user_account"

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register, name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    # PASSWORD RESET URLS
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),name='password_reset')    

]

