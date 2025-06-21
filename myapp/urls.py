from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('role/',views.role,name='role'),
    path('login/',views.login_page,name='user_login'),
    path('admin_access/',views.admin_access,name='admin_access_page'),
    path('register/',views.register_page,name='register_page'),
    
    path('admin_dash/',views.admin_dash),
    path('admin_project/',views.admin_project),
    path('admin_task/',views.admin_task),
    path('admin_user_manage/',views.admin_user_manage),
    path('admin_profile/',views.admin_profile),
    path('user_dash/',views.user_dash),
    path('user_task/',views.user_task),
    path('user_profile/',views.user_profile),
    path('user_notify/',views.user_notify),
    
    path('landing/',views.landing),
    
]
