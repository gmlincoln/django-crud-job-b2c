from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name="home"),
    path('add_job/', views.add_job, name="add_job"),
    path('all_jobs/', views.all_jobs, name="all_jobs"),
    path('single_job_view/<int:job_id>', views.single_job_view, name='single_job_view'),
    path('browse_jobs/', views.browse_jobs, name='browse_jobs'),
    
]