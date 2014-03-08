from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
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



