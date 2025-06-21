from django.shortcuts import render

# Create your views here.
def register_page(request):
    return render(request,'register.html')
def login_page(request):
    return render(request,'user_login.html')
def admin_dash(request):
    return render(request,'admin_dashboard.html')
def admin_project(request):
    return render(request,'admin_project_page.html')
def admin_task(request):
    return render(request,'admin_task_page.html')
def admin_user_manage(request):
    return render(request,'admin_user_management_page.html')
def admin_profile(request):
    return render(request,'admin_profile.html')
def user_dash(request):
    return render(request,'user_dashboard.html')
def user_task(request):
    return render(request,'user_task_page.html')
def user_profile(request):
    return render(request,'user_profile.html')
def user_notify(request):
    return render(request,'user_notification_page.html')
def landing(request):
    return render(request,'landing_page.html')
def home(request):
    return render(request,'home.html')
def role(request):
    return render(request,'role.html')
def admin_access(request):
    return render(request,'admin_access.html')
def admin_login(request):
    return render(request,'admin_login.html')