from django.contrib import admin
from .models import CustomerInquiry  # ✅ This is the only model you currently have

@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']
