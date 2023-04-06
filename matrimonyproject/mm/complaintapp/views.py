from django.contrib import messages
from django.shortcuts import render
from .models import Cport
# Create your views here.
def cmp(request):
    if request.method=='POST':
        cmp=request.POST["com"]
        email=request.POST["email"]
        img=request.POST['img']
        date=request.POST["date"]
        cport=Cport(cmp=cmp,email=email,img=img,date=date)
        print('user')
        cport.save()
        messages.success(request, "Complaint Has Been Successfully Registered")
        print('saved')
    return render(request,'comp.html')