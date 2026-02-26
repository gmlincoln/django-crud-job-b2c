from django.shortcuts import get_object_or_404, render, redirect

from django.contrib import messages

from django.db.models import Q 


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
    
    sort = request.GET.get('sort')
    
    if sort == 'asc':
        all_jobs = Job.objects.filter().order_by('job_title')
        
    elif sort == "desc":
        all_jobs = Job.objects.filter().order_by('-job_title')
    
    else:
        all_jobs = Job.objects.all()
    
    context = {
        'jobs': all_jobs
    }
    
    return render(request, 'Jobs/all_jobs.html', context)



def browse_jobs(request):
    query = request.GET.get('q')
    
    if query:
        all_jobs = Job.objects.filter(
            Q(job_title__icontains = query) |
            Q(company_name__icontains = query) |
            Q(category__icontains = query)
        )
   
    else:
        all_jobs = Job.objects.all()
    
    context = {
        'jobs': all_jobs,
        'query' : query
    }
    
    return render(request, 'Jobs/browse_jobs.html', context)



def single_job_view(request, job_id):
    
    job_data = get_object_or_404(Job, id=job_id)
    
    context = {
        'job':job_data
    }
    
    return render(request, 'Jobs/signle_job_view.html', context)

def delete_job(request, job_id):
    
    job = Job.objects.filter(id=job_id)
    job.delete()
        
    messages.success(request, 'Job Successfully Deleted!')
    return redirect('all_jobs')

def edit_job(request, job_id):
    
    job_data = get_object_or_404(Job, id=job_id)
    
    if request.method == "POST":
        job_data.job_title = request.POST.get('title')
        job_data.company_name = request.POST.get('company_name')
        
        if request.FILES.get('logo'):
            job_data.company_logo = request.FILES.get('logo')

        job_data.vacancy = request.POST.get('openings')
        job_data.category = request.POST.get('category')
        job_data.description = request.POST.get('description')
        job_data.skills = request.POST.get('skills')
        
        job_data.save()
        
        messages.success(request, 'Data Update Successfully!')
        return redirect('all_jobs')
        
                
    context ={
        'job' : job_data
    }
    
    return render(request, 'Jobs/edit_job.html', context)
    