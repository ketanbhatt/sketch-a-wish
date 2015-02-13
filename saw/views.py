from django.shortcuts import render
from saw.forms import UserForm, UserProfileForm

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

