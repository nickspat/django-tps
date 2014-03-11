from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from status_app.models import Project, Objective, Team, Person, StatusReport


def hello(request):
    return HttpResponse("Hello, world. You're at the project index.")

def index(request):
    return render_to_response('status_app/index.html')

def project_detail_old(request, project_name):
    return HttpResponse("You're looking at project %s." % project_name)

def project_list(request):
    context = RequestContext(request)
    project_list = Project.objects.all()
    template="status_app/project/list.html"
    params={'projects': project_list}
    return render_to_response(template, params, context)

def project_detail(request, project_id):
    context = RequestContext(request)
    project = Project.objects.get(id=project_id)
    template="status_app/project/details.html"
    params={'project': project}
    return render_to_response(template, params, context)

def report_list(request):
    context = RequestContext(request)
    report_list = StatusReport.objects.all()
    template="status_app/reports/list.html"
    params={'reports': report_list}
    return render_to_response(template, params, context)

def report_detail(request, statusreport_id):
    context = RequestContext(request)
    report = StatusReport.objects.get(id=statusreport_id)
    template="status_app/reports/details.html"
    params={'report': report}
    return render_to_response(template, params, context)

def team_list(request):
    context = RequestContext(request)
    team_list = Team.objects.all()
    template="status_app/team/list.html"
    params={'teams': team_list}
    return render_to_response(template, params, context)

def team_detail(request, team_id):
    context = RequestContext(request)
    team = Team.objects.get(id=team_id)
    template="status_app/team/details.html"
    params={'team': team}
    return render_to_response(template, params, context)


def person_list(request):
    context = RequestContext(request)
    people_list = Person.objects.all()
    template="status_app/person/list.html"
    params={'people': people_list}
    return render_to_response(template, params, context)

def person_detail(request, person_id):
    context = RequestContext(request)
    person = Person.objects.get(id=person_id)
    template="status_app/person/details.html"
    params={'person': person}
    return render_to_response(template, params, context)

class PersonList(ListView):
    model = Person
    template_name = 'status_app/person/list.html'

class PersonCreate(CreateView):
    model = Person
    template_name = 'status_app/person/form.html'
    success_url = reverse_lazy('person_list')

class PersonUpdate(UpdateView):
    model = Person
    template_name = 'status_app/person/form.html'
    success_url = reverse_lazy('person_list')

class PersonDelete(DeleteView):
    model = Person
    template_name = 'status_app/person/confirm_delete.html'
    success_url = reverse_lazy('person_list')


def status_detail(request, status_id):
    context = RequestContext(request)
    status = StatusReport.objects.get(id=status_id)
    template="status_app/person/status_details.html"
    params={'status': status}
    return render_to_response(template, params, context)

class StatusList(ListView):
    model = StatusReport
    template_name = 'status_app/person/status_list.html'

class StatusCreate(CreateView):
    model = StatusReport
    template_name = 'status_app/person/status_form.html'
    success_url = reverse_lazy('person_list')

class StatusUpdate(UpdateView):
    model = StatusReport
    template_name = 'status_app/person/status_form.html'
    success_url = reverse_lazy('person_list')

class StatusDelete(DeleteView):
    model = StatusReport
    template_name = 'status_app/person/confirm_delete.html'
    success_url = reverse_lazy('person_list')





class ProjectCreate(CreateView):
    model = Project
    template_name = 'status_app/project/form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'status_app/project/form.html'
    success_url = reverse_lazy('project_list')

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'status_app/project/confirm_delete.html'
    success_url = reverse_lazy('project_list')



class ObjectiveCreate(CreateView):
    model = Objective
    template_name = 'status_app/project/objective_form.html'
    success_url = reverse_lazy('project_list')

class ObjectiveUpdate(UpdateView):
    model = Objective
    template_name = 'status_app/project/objective_form.html'
    success_url = reverse_lazy('project_list')

class ObjectiveDelete(DeleteView):
    model = Objective
    template_name = 'status_app/project/confirm_delete.html'
    success_url = reverse_lazy('project_list')


class TeamCreate(CreateView):
    model = Team
    template_name = 'status_app/team/form.html'
    success_url = reverse_lazy('team_list')

class TeamUpdate(UpdateView):
    model = Team
    template_name = 'status_app/team/form.html'
    success_url = reverse_lazy('team_list')

class TeamDelete(DeleteView):
    model = Team
    template_name = 'status_app/team/confirm_delete.html'
    success_url = reverse_lazy('team_list')


