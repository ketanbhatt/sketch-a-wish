from django.shortcuts import render
from saw.models import Wish, Sketch, UserProfile
from saw.forms import UserForm, UserProfileForm, WishForm, SketchForm, GetWishForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse


# Create your views here.
def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})


def get_started(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('start'))

    if request.method == 'POST':

        which_submit = request.POST

        if 'submit_register' in which_submit:
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                registering_username = user.username
                registering_password = user.password

                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                profile.save()
                user = authenticate(username=registering_username, password=registering_password)
                login(request, user)
                return HttpResponseRedirect(reverse('start'))

            else:
                print user_form.errors, profile_form.errors

        elif 'submit_login' in which_submit:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('start'))

                else:
                    return HttpResponse("Your account is deactivated")

            else:
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'saw/get_started.html',
                  {'user_form' : user_form, 'profile_form' : profile_form})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('sketchawish'))


@login_required
def start(request):
    curr_user = UserProfile.objects.get(user = request.user)
    progress = curr_user.progress

    if request.method == "POST":

        which_submit = request.POST

        if 'submit_add_wish' in which_submit:
            wish_form = WishForm(request.POST)

            if wish_form.is_valid():
                wish = wish_form.save(commit=False)
                wish.wisher = request.user
                wish.save()

                curr_user = UserProfile.objects.get(user = request.user)
                curr_user.total_wished+=1
                curr_user.progress = 2
                curr_user.save()

                return HttpResponseRedirect(reverse('start'))

            else:
                print wish_form.errors

        elif 'submit_get_wish' in which_submit:
            get_wish_form = GetWishForm(request.POST, request=request)

            if get_wish_form.is_valid():
                to_sketch = get_wish_form.save(commit=False)
                to_sketch.sketcher = request.user
                to_sketch.save()
                Wish.objects.filter(pk=request.POST['wish']).update(locked=True, sketcher=request.user)

                curr_user = UserProfile.objects.get(user = request.user)
                curr_user.progress = 3
                curr_user.save()

                return HttpResponseRedirect(reverse('start'))

            else:
                print get_wish_form.errors

        elif 'submit_add_sketch' in which_submit:
            needed_pk = Sketch.objects.get(wish = request.POST['wish']).pk

            sketch_form = SketchForm(request.POST, request=request, instance = Sketch.objects.get(pk=needed_pk))

            if sketch_form.is_valid():
                sketch_form.save()
                Wish.objects.filter(pk=request.POST['wish']).update(sketched=True)
                curr_user = UserProfile.objects.get(user = request.user)
                curr_user.total_sketched+=1
                curr_user.progress = 1
                curr_user.save()

                return HttpResponseRedirect(reverse('sketchawish'))

            else:
                print sketch_form.errors

    else:
        wish_form = WishForm()
        get_wish_form = GetWishForm(request=request)
        sketch_form = SketchForm(request=request)

    return render(request, 'saw/start.html', {'wish_form': wish_form, 'get_wish_form': get_wish_form, 'sketch_form': sketch_form, 'progress': progress})
