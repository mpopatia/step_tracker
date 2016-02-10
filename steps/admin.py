from django.contrib import admin
from steps.models import StepCount, EmailCounter

# Register your models here.

class StepCountDetails(admin.ModelAdmin):
    list_display = ['owner', 'owner_email', 'steps', 'dateCreated']
    list_filter = ['dateCreated']

class EmailDetails(admin.ModelAdmin):
    list_display = ['dateCreated']

admin.site.register(StepCount, StepCountDetails)
admin.site.register(EmailCounter, EmailDetails)
