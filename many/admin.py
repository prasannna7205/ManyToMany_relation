from django.contrib import admin
from many.models import Student

# Register your models here.
class display(admin.ModelAdmin):
    list_display=['song_name','song_durection','get']
admin.site.register(Student,display)

















