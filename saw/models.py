from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)
    country = models.CharField(max_length=128)
    total_sketched = models.IntegerField(default=0)
    total_wished = models.IntegerField(default=0)
    progress = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username


class Wish(models.Model):
    content = models.CharField(max_length=500)
    wisher = models.ForeignKey(User, related_name='wisher_of_wish')
    sketcher = models.ForeignKey(User, related_name='sketcher_of_wish', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    locked = models.BooleanField(default=False)
    sketched = models.BooleanField(default=False)

    class Meta():
        verbose_name_plural = 'Wishes'

    def __unicode__(self):
        return self.content


class Sketch(models.Model):
    wish = models.ForeignKey(Wish)
    wisher = models.ForeignKey(User, related_name='wisher_of_sketch', null=True)
    sketcher = models.ForeignKey(User, related_name='sketcher_of_sketch', null=True)
    sketch_image = models.ImageField(upload_to='sketches/', blank=True)
    likes = models.IntegerField(default=0)
    assigned_on = models.DateTimeField(auto_now_add=True)
    submitted_on = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural = 'Sketches'

    def __unicode__(self):
        return "Sketch for \"" + self.wish.content + "\""
