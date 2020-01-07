from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages, auth

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            return redirect('superuser')

        else:
            # messages.error(request, 'Invalid credentials')
            return redirect('login')

class LogOutnView(View):
    def post(self, request):
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return redirect('login')