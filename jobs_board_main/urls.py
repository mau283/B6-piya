from django.urls import path
from .views import get_jobs, single_job, subscribe



urlpatterns = [
    path('jobs/', get_jobs, name = "all_jobs"),
    path('jobs/<int:id>/', single_job, name = "Single_job"),
    path('jobs/<int:id>/subscribe/', subscribe, name = "Subs"),
    
]
