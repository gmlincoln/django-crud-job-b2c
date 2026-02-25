from django.contrib import admin
from .models import Job 

# Register your models here.
# admin.site.register(Job)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'vacancy', 'category', 'company_logo')
    list_filter = ('category',)
    search_fields = ('job_title', 'company_name')
    ordering = ('created_at', )