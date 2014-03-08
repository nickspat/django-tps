from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128, unique=True)    
    corpid = models.CharField(max_length=10)    
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=128)
    managerId = models.OneToOneField(Person)    
    members = models.ManyToManyField(Person, related_name='names', null=True,blank=True)
    def __unicode__(self):
        return self.name
        
class Project(models.Model):
    STATE = (
             (u'GREEN',u'GREEN'),
             (u'RED',u'RED'),
             (u'YELLOW',u'YELLOW'))
    owner = models.ForeignKey(Person)
    name = models.CharField(max_length=128, unique=True)
    state = models.CharField(max_length=10, choices=STATE)    
    teams = models.ManyToManyField(Team,null=True,blank=True)
    
    def __unicode__(self):
        return self.name

class Objective(models.Model):
    STATE = (
             (u'OPEN',u'OPEN'),
             (u'INPROGRESS',u'INPROGRESS'),
             (u'COMPLETED',u'COMPLETED'),
             (u'CANCELLED',u'CANCELLED'))
    project = models.ForeignKey(Project) 
    title = models.CharField(max_length=128)
    state = models.CharField(max_length=24, choices=STATE)
    percentage_completed = models.PositiveSmallIntegerField()    
    parentObjId = models.PositiveIntegerField(default=0)   
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(Person)

    def __unicode__(self):
        return self.title




class StatusReport(models.Model):
    reporter = models.ForeignKey(Person)
    status_message = models.CharField(max_length=10000)
    project = models.CharField(max_length=100, null=True,blank=True)
    start_date = models.DateField()
    due_date = models.DateField()
    
    def __unicode__(self):
        return unicode(self.reporter)