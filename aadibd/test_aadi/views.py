from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Interview,Session,Applicants
# Create your views here.
class IndexView(generic.ListView):
    template_name='index.html'
    context_object_name='interviews'
    def get_queryset(self):
        return Interview.objects.all()
class SessionDetailView(generic.DetailView):
    model=Interview
    context_object_name='sessions'
    template_name='session_detail.html'