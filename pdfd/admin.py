
from django.contrib import admin
from .models import notices

class CustomNoticesAdmin(admin.ModelAdmin):
    list_display = ('title', 'downloaded_timestamp')

admin.site.register(notices, CustomNoticesAdmin)
