from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wish(models.Model):
    content = models.CharField(max_length=500)
    wisher = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Wishes'

    def __unicode__(self):
        return self.content


class Sketch(models.Model):
    wish = models.ForeignKey(Wish)
    title = models.CharField(max_length=128)
    sketcher = models.ForeignKey(User)
    image_temp = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Sketches'

    def __unicode__(self):
        return self.title
