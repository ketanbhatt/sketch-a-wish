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

def add_wish(content, wisher):
    c = Wish.objects.get_or_create(content = content, wisher = wisher)

# Start execution here!
if __name__ == '__main__':
    print "Starting SAW population script..."
    populate()
