from django.urls import path
from job_app import views



urlpatterns = [

    path('job-details/<int:job_id>/', views.job_details, name='job-details'),
    path('', views.joblist, name='joblist'),
    path('categoy-wise-jobs/<slug:category_slug>/', views.Category_wise_jobs, name='categoy-wise-jobs'),
    path('search/', views.search_jobs, name='search'),
    path('contact', views.contact, name='contact' ),
   
   
]