from django.contrib import admin
from status_app.models import Project, Objective,Team, Person, StatusReport

admin.site.register(Project)
admin.site.register(Objective)
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(StatusReport)