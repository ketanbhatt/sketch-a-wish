from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})
