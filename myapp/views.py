from django.shortcuts import render

# Create your views here.
def register_page(request):
    return render(request,'register.html')
def login_page(request):
    return render(request,'login.html')
def admin_dash(request):
    return render(request,'admin_dashboard.html')

