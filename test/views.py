from django.shortcuts import render, redirect, resolve_url
from .forms import TestForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    test_info = TestForm(request.POST)
    return render(request, 'test/test.html', {'test_info':test_info})

@csrf_exempt
def saveTest(request):
    test_info = TestForm(request.POST)
    test_info.save()
    return render(request, 'popupAndRedirect.html', {'message':"success", 'redirectUrl':"http://127.0.0.1:8000/test/"})
