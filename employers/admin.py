from django.contrib import admin
from .models import Employer

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person_name', 'email', 'user', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['company_name', 'contact_person_name', 'email']
    ordering = ['company_name']
    fieldsets = (
        (None, {'fields': ('user', 'company_name', 'contact_person_name')}),
        ('Contact Info', {'fields': ('email', 'phone_number', 'address')}),
        ('Metadata', {'fields': ('created_at',)}),
    )
    readonly_fields = ['created_at']
