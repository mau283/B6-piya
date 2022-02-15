
from django.shortcuts import render
from .models import Job, Subscriber, Subscription
from .signals import new_subscriber
from django.db import transaction



# Create your views here.

def get_jobs(request):
    jobs= Job.objects.all()
    return render(request, "jobs.html", {"jobs": jobs})

def single_job(request, id):
    job = Job.objects.get(id=id)
    return render(request, "job.html", {"job":job})

def subscribe(request, id):
    # with transaction.atomic():
        job = Job.objects.get(pk=id)
        data = Subscriber.objects.filter(email = request.POST['email'])
        if data.exists():
            sub = data[0]
        else:
            sub = Subscriber(email= request.POST['email'])
            sub.save()

        subscription = Subscription(user = sub, job = job)
        subscription.save()
        print(job, request.POST['email'])
        new_subscriber.send(sender = Subscription, job = job, subscriber = sub)
        payload = {
            'job':job,
            'email': request.POST['email']
        }
        return render(request, 'subsrcribed.html', {'payload': payload})