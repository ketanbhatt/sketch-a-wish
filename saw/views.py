from django.shortcuts import render
from saw.forms import UserForm, UserProfileForm, WishForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'saw/register.html',
                  {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/sketchawish/')

            else:
                return HttpResponse("Your account is deactivated")

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'saw/login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/sketchawish/')


@login_required
def add_wish(request):
    if request.method == "POST":
        wish_form = WishForm(request.POST)

        if wish_form.is_valid():
            wish = wish_form.save(commit=False)
            wish.wisher = request.user
            wish.save()

            return sketchawish(request)

        else:
            print wish_form.errors

    else:
        wish_form = WishForm()

    return render(request, 'saw/add_wish.html', {'wish_form': wish_form})



