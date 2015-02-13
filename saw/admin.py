from django.contrib import admin
from saw.models import Wish, Sketch, UserProfile

# Register your models here.
class WishAdmin(admin.ModelAdmin):
    list_display = ('content', 'wisher', 'created_on')

class SketchAdmin(admin.ModelAdmin):
    list_display = ('title', 'sketcher', 'likes', 'created_on')

admin.site.register(Wish, WishAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(UserProfile)
