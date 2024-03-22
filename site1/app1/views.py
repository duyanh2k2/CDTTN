from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Question,BenhNhan
from collections import deque
from .form import MyForm,NhapBN
import time
# Create your views here.

dq= deque()

def nhapbn(request):
    a= NhapBN()
    return render(request,"app1/nhapbn.html",{"form":a})

def savebn(request):
    if request.method == "POST":
        g = NhapBN(request.POST)
        if g.is_valid():
            saveg=BenhNhan(NameBN= g.cleaned_data['NameBN'],
                           Date= g.cleaned_data['Date'],
                           DateK= g.cleaned_data['DateK'],
                           CCCD= g.cleaned_data['CCCD'])
            saveg.save()
            
            UT=g.cleaned_data['UT']
            if(UT==False):
              dq.append(saveg)
            else:
                dq.appendleft(saveg)

            return redirect('hienbn')
        else:
            return HttpResponse("sai")
    else:
        return HttpResponse("ko phải post")      
def hien(request):
    return render(request,"app1/hienbn.html",{"dq":dq})