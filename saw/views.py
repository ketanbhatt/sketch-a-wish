from __future__ import absolute_import
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Wish, Sketch, UserProfile
from .forms import WishForm, SketchForm, GetWishForm
from .utils import *


def sketchawish(request):
    return render(request, 'saw/sketchawish.html', {})


def get_started(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('start'))

    return render(request, 'saw/get_started.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('sketchawish'))


@login_required
def start(request):
    curr_user = UserProfile.objects.get(user=request.user)
    progress = curr_user.progress

    if request.method == "POST":

        which_submit = request.POST

        if 'submit_add_wish' in which_submit:
            wish_form = WishForm(request.POST)

            if wish_form.is_valid():
                wish = wish_form.save(commit=False)
                wish.wisher = request.user
                wish.save()

                curr_user = UserProfile.objects.get(user=request.user)
                curr_user.total_wished += 1
                curr_user.progress = 2
                curr_user.save()
            else:
                messages.error(request, 'You don\'t have anything to wish?', fail_silently=True)

            return HttpResponseRedirect(reverse('start'))

        elif 'submit_get_wish' in which_submit:
            get_wish_form = GetWishForm(request.POST, request=request)

            if get_wish_form.is_valid():
                to_sketch = get_wish_form.save(commit=False)
                to_sketch.sketcher = request.user
                to_sketch.save()
                Wish.objects.filter(pk=request.POST['wish']).update(locked=True, sketcher=request.user)

                curr_user = UserProfile.objects.get(user=request.user)
                curr_user.progress = 3
                curr_user.save()

                return HttpResponseRedirect(reverse('start'))

            else:
                print get_wish_form.errors

        elif 'submit_add_sketch' in which_submit:
            needed_pk = Sketch.objects.get(wish=request.POST['wish']).pk

            sketch_form = SketchForm(request.POST, request=request, instance=Sketch.objects.get(pk=needed_pk))

            if sketch_form.is_valid():
                sketch = sketch_form.save(commit=False)
                if 'sketch_image' in request.FILES:
                    fobject = request.FILES['sketch_image']

                    if valid_image_mimetype(fobject):
                        sketch.sketch_image.save('{0}_sketch.jpg'.format(sketch.pk), request.FILES['sketch_image'])
                        sketch.wisher = Wish.objects.get(pk=request.POST['wish']).wisher
                        sketch.sketcher = request.user
                        sketch.save()

                        Wish.objects.filter(pk=request.POST['wish']).update(sketched=True)
                        Wish.objects.filter(wisher=request.user, is_live=False).update(is_live=True)

                        curr_user = UserProfile.objects.get(user=request.user)
                        curr_user.total_sketched += 1
                        curr_user.progress = 1
                        curr_user.save()
                        return HttpResponseRedirect(reverse('sketchawish'))
                    else:
                        messages.error(request, 'Wrong filetype uploaded', fail_silently=True)
                        return HttpResponseRedirect(reverse('start'))

                else:
                    messages.error(request, 'Come on! Where is the sketch?', fail_silently=True)
                    return HttpResponseRedirect(reverse('start'))

            else:
                print sketch_form.errors

    else:
        wish_form = WishForm()
        get_wish_form = GetWishForm(request=request)
        sketch_form = SketchForm(request=request)

    return render(request, 'saw/start.html', {'wish_form': wish_form, 'get_wish_form': get_wish_form, 'sketch_form': sketch_form, 'progress': progress})


@login_required
def user_profile(request):
    curr_user = UserProfile.objects.get(user=request.user)
    curr_user_sketches = Sketch.objects.filter(sketcher=request.user)
    curr_user_wishes = Wish.objects.filter(wisher=request.user)
    dict_for_template = {'curr_user': curr_user, 'user_sketches': curr_user_sketches, 'user_wishes': curr_user_wishes}
    return render(request, 'saw/profile.html', dict_for_template)
