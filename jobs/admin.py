from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_by', 'posted_date', 'is_active')
    list_filter = ('job_type', 'category', 'is_active', 'posted_date')
    search_fields = ('title', 'company', 'location', 'description')
    date_hierarchy = 'posted_date'

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'application_date', 'status')
    list_filter = ('status', 'application_date')
    search_fields = ('job__title', 'applicant__username', 'cover_letter')