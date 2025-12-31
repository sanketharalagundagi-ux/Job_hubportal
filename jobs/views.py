from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from jobs.models import Job

def home(request):
    # Get 4 featured/active jobs from database
    featured_jobs = Job.objects.filter(is_active=True)[:4]
    
    context = {
        'featured_jobs': featured_jobs,
    }
    return render(request, 'home.html', context)

def job_list(request):
    # Get all active jobs
    jobs = Job.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    context = {
        'jobs': jobs,
        'search_query': search_query,
    }
    return render(request, 'job_list.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)
    return render(request, 'job_detail.html', {'job': job})