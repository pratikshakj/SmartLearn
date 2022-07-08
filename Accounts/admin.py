from django.contrib import admin
from .models import profile,classroom,timetable,attendance,posts
# Register your models here.
class userad(admin.ModelAdmin):
    list_display=('user','Uid','role')

class classad(admin.ModelAdmin):
    list_display=('class_name','class_subject','admin')

admin.site.register(profile,userad)
admin.site.register(classroom,classad)
admin.site.register(timetable)
admin.site.register(attendance)
admin.site.register(posts)
