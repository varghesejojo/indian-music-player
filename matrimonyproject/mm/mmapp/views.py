
# Create your views here.

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect












def log_in(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            # context["user"] = name_r
            # context["id"] = request.user.id
            # print('user')
            return render(request, 'thank.html')

        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'login.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'login.html', context)






def register(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            messages.info(request, "You have successfully register.")
            return render(request, 'login.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html', context)





def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("mmapp:login")
def thank(request):
    return render(request,'thank.html')
def contact(request):
    return  render(request,'contact.html')




