import logging
import os

from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings



class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponseRedirect(f"{settings.REACT_APP_URL[0]}")

def index(request):
    return JsonResponse({'Message': "Hello"})