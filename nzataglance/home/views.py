from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour, Agent

def home(request):
     # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(request, 'home.html', context={ 'num_visits': num_visits})

def tour_detail(request, id):
    try:
        tour = Tour.objects.get(id=id)
    except Tour.DoesNotExist:
        raise Http404('Tour not found')
    return render(request, 'tour_detail.html', {'tour': tour})

def agent_detail(request, id):
    try:
        agent = Agent.objects.get(id=id)
    except Agent.DoesNotExist:
        raise Http404('Tour not found')
    return render(request, 'agent_detail.html', {'agent': agent})

from django.views import generic

class TourListView(generic.ListView):
    model = Tour
    paginate_by = 10

# way to restrict access to logged-in users in your class-based views
class AgentListView(generic.ListView):
    model = Agent
    paginate_by = 10


class TourDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tour


class AgentDetailView(generic.DetailView):
    model = Agent
