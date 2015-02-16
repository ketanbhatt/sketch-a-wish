from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wish(models.Model):
    content = models.CharField(max_length=500)
    wisher = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    locked = models.BooleanField(default=False)

    class Meta():
        verbose_name_plural = 'Wishes'

    def __unicode__(self):
        return self.content


class Sketch(models.Model):
    wish = models.ForeignKey(Wish)
    sketcher = models.ForeignKey(User)
    image_temp = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    assigned_on = models.DateTimeField(auto_now_add=True)
    submitted_on = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name_plural = 'Sketches'

    def __unicode__(self):
        return "Sketch for \""+ self.wish.content + "\""

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    country = models.CharField(max_length=128, default="Somewhere in the World" )
    sketched = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
