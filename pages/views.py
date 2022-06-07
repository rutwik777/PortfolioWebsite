from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def portfolio(request):
    return render(request, 'pages/portfolio-details.html')

def portfolio2(request):
    return render(request, 'pages/portfolio-details2.html')

def portfolio3(request):
    return render(request, 'pages/portfolio-details3.html')

def portfolio4(request):
    return render(request, 'pages/portfolio-details4.html')

def portfolio5(request):
    return render(request, 'pages/portfolio-details5.html')

def portfolio6(request):
    return render(request, 'pages/portfolio-details6.html')

def personal(request):
    return render(request,'pages/personal.html')