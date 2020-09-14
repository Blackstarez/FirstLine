from django.shortcuts import render

# Create your views here.

def addPostView(request):
return render(request, 'post/addPostView.html')