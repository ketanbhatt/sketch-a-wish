import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sketch_a_wish.settings')

import django
django.setup()

from saw.models import Wish
from django.contrib.auth.models import User

kb = User.objects.get()


def populate():
    add_wish(content="wish 1", wisher=kb)


def add_wish(content, wisher):
    Wish.objects.get_or_create(content=content, wisher=wisher, is_live=True)

# Start execution here!
if __name__ == '__main__':
    print "Starting SAW population script..."
    populate()
