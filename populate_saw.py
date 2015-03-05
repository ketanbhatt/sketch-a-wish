import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sketch_a_wish.settings')

import django
django.setup()

from saw.models import Wish
from django.contrib.auth.models import User

kb = User.objects.get()


def populate():
    add_wish(content="wish 1", wisher=kb)
    add_wish(content="wish 2", wisher=kb)
    add_wish(content="wish 3", wisher=kb)
    add_wish(content="wish 4", wisher=kb)
    add_wish(content="wish 5", wisher=kb)
    add_wish(content="wish 6", wisher=kb)
    add_wish(content="wish 7", wisher=kb)
    add_wish(content="wish 8", wisher=kb)
    add_wish(content="wish 9", wisher=kb)
    add_wish(content="wish 10", wisher=kb)
    add_wish(content="wish 11", wisher=kb)
    add_wish(content="wish 12", wisher=kb)
    add_wish(content="wish 13", wisher=kb)
    add_wish(content="wish 14", wisher=kb)
    add_wish(content="wish 15", wisher=kb)


def add_wish(content, wisher):
    Wish.objects.get_or_create(content=content, wisher=wisher, is_live=True)

# Start execution here!
if __name__ == '__main__':
    print "Starting SAW population script..."
    populate()
