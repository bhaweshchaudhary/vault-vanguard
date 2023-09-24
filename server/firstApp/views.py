from django.shortcuts import render, HttpResponse
from .forms import MyFileUploadForm
from .models import file_upload
import requests
import ipfshttpclient


def index(request):
    if request.method == 'POST':
        c_form = MyFileUploadForm(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files']
            file_upload(file_name=name, my_file=files).save()

            # Upload the file to IPFS
            client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
            res = client.add(files.temporary_file_path())
            ipfs_hash = res['Hash']

            return HttpResponse(f"File uploaded to IPFS with hash: {ipfs_hash}")
        else:
            return HttpResponse("Error")
    else:
        context = {
            'form': MyFileUploadForm()
        }
        return render(request, 'index.html', context)


def show_file(request):
    all_data = file_upload.objects.all()

    context = {
        'data': all_data
    }

    return render(request, 'view.html', context)