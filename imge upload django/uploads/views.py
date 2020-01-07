from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.files.storage import FileSystemStorage
from PIL import Image
from io import StringIO

class UploadsView(View):
    def get(self, request):
        return render(request, 'uploads/upload.html')

    def post(self, request):
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage(location='media/Nitai')
        # Resize before upload
        

        name = fs.save(uploaded_file.name, uploaded_file)
        context = {
            'url':fs.url(name)
        }
        # return HttpResponse('Working')
        return render(request, 'uploads/upload.html', context)