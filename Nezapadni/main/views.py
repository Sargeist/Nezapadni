from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def story(request):
    return render(request, 'pages/story.html')

def vision(request):
    return render(request, 'pages/vision.html')
