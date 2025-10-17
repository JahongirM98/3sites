from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at", "message")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("created_at",)
