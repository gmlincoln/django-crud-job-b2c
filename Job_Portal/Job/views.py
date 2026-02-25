from django.shortcuts import get_object_or_404, render, redirect

from django.contrib import messages



from .models import Job

# Create your views here.
def home(request):
    
    return render(request, 'Jobs/index.html')

def add_job(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        name = request.POST.get('company_name')
        logo = request.FILES.get('logo')
        openings = request.POST.get('openings')
        category = request.POST.get('category')
        description = request.POST.get('description')
        skills = request.POST.get('skills')
        
        Job.objects.create(
            job_title = title,
            company_name = name,
            company_logo = logo,
            vacancy = openings,
            category = category,
            description = description,
            skills = skills
        )
        
        messages.success(request, 'Job Successfully Added!')

        return redirect('all_jobs')
        
    
    return render(request, 'Jobs/add_job.html')


def all_jobs(request):
    
    all_jobs = Job.objects.all()
    
    context = {
        'jobs': all_jobs
    }
    
    return render(request, 'Jobs/all_jobs.html', context)



def browse_jobs(request):
    all_jobs = Job.objects.all()
    
    context = {
        'jobs': all_jobs
    }
    
    return render(request, 'Jobs/browse_jobs.html', context)



def single_job_view(request, job_id):
    
    job_data = get_object_or_404(Job, id=job_id)
    
    context = {
        'job':job_data
    }
    
    return render(request, 'Jobs/signle_job_view.html', context)