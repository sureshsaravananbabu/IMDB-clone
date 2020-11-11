from django.contrib import admin
from .models import movie,movielinks,cast
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    pass

admin.site.register(movielinks)
admin.site.register(cast)
admin.site.register(movie, MyModelAdmin)

# Register your models here.
