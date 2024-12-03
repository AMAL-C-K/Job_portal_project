from django.shortcuts import render
from . models import Category, Jobs
from accounts_app.models import Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required




@login_required(login_url='/')
def joblist(request):
    profile=None
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        pass    
    jobs = Jobs.objects.all().order_by('-date_added')
    category = Category.objects.all()
    return render(request, 'joblist.html',{'jobs':jobs,'profile':profile, 'category':category})  

   

@login_required(login_url='/')
def job_details(request, job_id):
    job = Jobs.objects.get(id=job_id)
    return render(request, 'details.html', {'job':job})

@login_required(login_url='/')
def Category_wise_jobs(request, category_slug):
    jobs = Jobs.objects.filter(category__slug=category_slug).order_by('-date_added')
    category = Category.objects.get(slug=category_slug)
    return render(request, 'categorywise_jobs.html', {'jobs':jobs,'category':category})


@login_required(login_url='/')
def search_jobs(request):
    jobs = None
    q = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        jobs = Jobs.objects.filter(Q(role__job_role__contains=query) | Q(experience__contains=query)).order_by('-date_added')
    return render(request, 'search.html', {'query':query, 'jobs':jobs})

def contact(request):
    return render(request, 'contact.html')