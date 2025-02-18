from django.contrib import admin
from .models import ContactUs, Subscription
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

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'created_at'
    ]
    list_filter = ['created_at']
    search_fields = ['email']