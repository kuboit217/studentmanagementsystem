from django.contrib import messages
from django.contrib.auth import login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from studentmanagementapp.EmaiLBackEnd import EmailBackEnd


def ShowDemo(request):
    return render(request, 'demo.html')


def ShowLoginPage(request):
    return render(request, 'login_page.html')


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allow</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request, 'Invalid Login Details')
            return HttpResponseRedirect('/')


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse('Email: ' + request.user.email + 'User_Type: ' + request.user.user_type)
    else:
        return HttpResponse('Please Login First')


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
