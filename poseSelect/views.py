from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'poseSelect/index.html')

def fourbyone(request):
    print(request)
    image_url = request.GET.get('image_url')
    idx = request.GET.get('index')
    print(image_url)
    return render(request, 'poseSelect/fourbyone.html', {'image_url' : image_url, 'idx' : idx})

def fourbyone_1(request):
    return render(request, 'poseSelect/fourbyone_1.html')

def fourbyone_image(request):
    image_url = request.POST.get('image_url')
    print(image_url)
    print("=========================")
    return redirect(request, 'poseSelect/fourbyone.html', {'image_url' : image_url})

def twobytwo(request):
    return render(request, 'poseSelect/twobytwo.html')

def fourbyone_2(request):
    return render(request, 'poseSelect/fourbyone_2.html')

def fourbyone_3(request):
    return render(request, 'poseSelect/fourbyone_3.html')

def fourbyone_4(request):
    return render(request, 'poseSelect/fourbyone_4.html')