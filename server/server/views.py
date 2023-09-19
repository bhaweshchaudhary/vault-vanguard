from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import View

class ReactAppProxyView(View):
    def get(self, request):
        if not settings.DEBUG:
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(settings.REACT_DEV_SERVER_URL)


