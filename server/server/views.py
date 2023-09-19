from django.http import HttpResponseRedirect
from django.conf import settings

def encryptData(request):
    return HttpResponseRedirect(settings.REACT_DEV_SERVER_URL)