# image-upload

Let's create a app name uploads.
Then create a template and write some html code for file upload.
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="document">
    <button type="submit">Upload file</button>
</form>

Note: Make sure you use enctype in form tag.
Like: enctype="multipart/form-data"


Ok, now we can take file from our view method.
def post(self, request):
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        return HttpResponse('Working')

Here is a importent things. Files are dictionarys.
So, we need to use request.FILES['file_inputtag_name']

We can also take file name and file size in our view.
Example:
print(uploaded_file.name)
print(uploaded_file.size)

Now we need some setup for where actually file will save.
Go to settings.py and add some code.
#Media folder settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

Then, configure in your main urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
[Note: This line use only use in development mode. Not in Production mode...]

And import those:
from django.conf import settings
from django.conf.urls.static import static


Everything is ok... Now we need to upload our file.
---------------------------------------------------
Import the FileSystemStorage
from django.core.files.storage import FileSystemStorage
Then create a object of FileSystemStorage and then save.
def post(self, request):
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return HttpResponse('Working')

Here in save function we can see 2 arguments.
first one is filename, second one is file itself.

We can see the uploaded file in our browser.
got to your browser and write the url as like:
http://127.0.0.1:8000/media/Guru.png 
Here media is not your folder. It's your MEDIA_URL name which you already define in your settings.py file.

Let's show the uploaded image url.
In view make some changes.
        name = fs.save(uploaded_file.name, uploaded_file)
        context = {
            'url':fs.url(name)
        }
        return render(request, 'uploads/upload.html', context)

In template make some changes.
{% if url %}
    <p>Uploaded file: <a href="{{ url }}">{{ url }}</a></p>
{% endif %}


We can save our file to a specific folder.
fs = FileSystemStorage(location='media/Nitai')
It will save in media folder subfolder Nitai.
