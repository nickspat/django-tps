from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
        
class Project(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Objective(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=128)
    status = models.CharField(max_length=128)


    def __unicode__(self):
        return self.title






class Person(models.Model):
    name = models.CharField(max_length=128, unique=True)
    groups = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.name
