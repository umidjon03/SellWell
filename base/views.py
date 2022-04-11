from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/index.html')


def test(request):
    return render(request, 'base/test.html')