from saw.models import UserProfile
from requests import request, HTTPError
from django.core.files.base import ContentFile

def save_user_profile(backend, user, response, is_new=False, *args, **kwargs):
    if is_new:
        if backend.name == 'facebook':
            url = "http://graph.facebook.com/%s/picture" % response["id"]
            try:
                response_picture = request('GET', url, params={'type': 'large'})
                response_picture.raise_for_status()
            except HTTPError:
                pass
            else:
                UserProfile.objects.get_or_create(user=user, country=response.get('timezone'))
                profile = UserProfile.objects.get(user=user)
                profile.profile_photo.save('{0}_social.jpg'.format(user.email), ContentFile(response_picture.content))
                profile.save()

        elif backend.name == 'google-oauth2':
            url = response["image"]
            UserProfile.objects.get_or_create(user=user)

    else:
        if backend.name == 'facebook':
            UserProfile.objects.get_or_create(user=user)

        elif backend.name == 'google-oauth2':
            UserProfile.objects.get_or_create(user=user)

