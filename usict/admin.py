from django.contrib import admin
from .models import Paper
# Register your models here.

class PaperAdmin(admin.ModelAdmin):
    list_display = ('course', 'semester', 'subject', 'year')

admin.site.register(Paper, PaperAdmin)