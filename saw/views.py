from django.shortcuts import render
from saw.models import Wish, Sketch, UserProfile
from saw.forms import UserForm, UserProfileForm, WishForm, SketchForm, GetWishForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# Create your views here.
def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})


def get_started(request):

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
                return HttpResponseRedirect('/sketchawish')

            else:
                print user_form.errors, profile_form.errors

        else:
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
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'saw/get_started.html',
                  {'user_form' : user_form, 'profile_form' : profile_form})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/sketchawish/')


@login_required
def add_wish(request):

    curr_user = UserProfile.objects.get(user = request.user)
    if curr_user.total_wished >= curr_user.total_sketched :
        messages.info(request, 'You need to sketch first')
        return HttpResponseRedirect('/sketchawish/get_wish/')

    if request.method == "POST":
        wish_form = WishForm(request.POST)

        if wish_form.is_valid():
            wish = wish_form.save(commit=False)
            wish.wisher = request.user
            wish.save()

            curr_user = UserProfile.objects.get(user = request.user)
            curr_user.total_wished+=1
            curr_user.save()

            return sketchawish(request)

        else:
            print wish_form.errors

    else:
        wish_form = WishForm()

    return render(request, 'saw/add_wish.html', {'wish_form': wish_form})

@login_required
def get_wish(request):

    wishes_to_get = Wish.objects.exclude(wisher = request.user).filter(pk__in = Wish.objects.filter(locked=False)[:3].values_list('pk'))
    if wishes_to_get.count() < 1 :
        messages.info(request, 'Sorry there are no available wishes at the moment!')
        return HttpResponseRedirect('/sketchawish/')

    if request.method == "POST":
        get_wish_form = GetWishForm(request.POST, request=request)

        if get_wish_form.is_valid():
            to_sketch = get_wish_form.save(commit=False)
            to_sketch.sketcher = request.user
            to_sketch.save()
            Wish.objects.filter(pk=request.POST['wish']).update(locked=True, sketcher=request.user)

            return sketchawish(request)

        else:
            print get_wish_form.errors

    else:
        get_wish_form = GetWishForm(request=request)

    return render(request, 'saw/get_wish.html', {'get_wish_form': get_wish_form})

@login_required
def add_sketch(request):

    wishes_to_sketch = Wish.objects.filter(sketcher=request.user).filter(sketched=False)
    if wishes_to_sketch.count() < 1 :
        messages.info(request, 'You need to select a wish first')
        return HttpResponseRedirect('/sketchawish/get_wish/')

    if request.method == "POST":

        needed_pk = Sketch.objects.get(wish = request.POST['wish']).pk

        sketch_form = SketchForm(request.POST, request=request, instance = Sketch.objects.get(pk=needed_pk))

        if sketch_form.is_valid():
            sketch_form.save()
            Wish.objects.filter(pk=request.POST['wish']).update(sketched=True)
            curr_user = UserProfile.objects.get(user = request.user)
            curr_user.total_sketched+=1
            curr_user.save()

            return sketchawish(request)

        else:
            print sketch_form.errors

    else:
        sketch_form = SketchForm(request=request)


    return render(request, 'saw/add_sketch.html', {'sketch_form': sketch_form})
