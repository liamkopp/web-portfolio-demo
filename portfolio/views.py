from django.shortcuts import render
from django.views import generic
# Create your views here.
from portfolio.models import Project, Type

# def index(request):
#     """View function for home page of site."""
#     context = {}
#
#     return render(request, 'projects.html', context=context)

class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projects.html'