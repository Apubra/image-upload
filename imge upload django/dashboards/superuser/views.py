from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages, auth

class SuperUserView(View):
    def get(self, request):
        return render(request, 'dashboards/super user/super user dashboard.html')