from django.contrib import admin

from .models import Announcement, Category

admin.site.register(Announcement)
admin.site.register(Category)
