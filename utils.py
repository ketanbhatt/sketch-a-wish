from saw.models import UserProfile

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        UserProfile.objects.get_or_create(user=user, country=response.get('timezone'))

    elif backend.name == 'google-oauth2':
        UserProfile.objects.get_or_create(user=user)
