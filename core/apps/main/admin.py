from django.contrib import admin
from .models import ContactUs
# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'text',
        'created_at'
    ]
    list_filter = ['created_at']
    search_fields = ['name',
                     'email',]