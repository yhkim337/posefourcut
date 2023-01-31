from django.shortcuts import render

def index(request):
    return render(request, 'poseSelect/index.html')

def fourbyone(request):
    return render(request, 'poseSelect/fourbyone.html')
