from __future__ import absolute_import
from django.contrib import admin
from .models import Wish, Sketch, UserProfile


class WishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'wisher', 'sketcher', 'created_on', 'is_live', 'locked', 'sketched')


class SketchAdmin(admin.ModelAdmin):
    model = Sketch
    list_display = ('pk', 'sketch_image', 'wish', 'wisher', 'sketcher', 'likes', 'assigned_on', 'submitted_on')


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'profile_photo', 'get_email', 'country', 'progress', 'total_sketched', 'total_wished')

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "Email ID"


admin.site.register(Wish, WishAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
