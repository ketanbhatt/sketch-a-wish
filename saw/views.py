from django.shortcuts import render

# Create your views here.
def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})
