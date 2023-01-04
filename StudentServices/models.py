from django.db import models

from website.models import Faculty

# Create your models here.
class Artsupdates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField( default="No data")
    date = models.DateField()
    def __str__(self):
        return self.title

class ArtsEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='arts/events')
    def __str__(self):
        return self.title


class artsTeamStatus(models.Model):
    TEAMS = (("cetus","cetus"),("pegasus","pegasus"),("taurs","taurs"),("lupus","lupus"))
    teamname = models.CharField(max_length=100,choices=TEAMS)
    logo = models.ImageField(upload_to='arts/teams/logos',default='arts/teams/logos/default.png')
    score = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    color = models.CharField(max_length=100,default='red-700')
    image = models.ImageField(upload_to='arts/teams')
    def __str__(self):
        return self.teamname

class ArtsGallery(models.Model):
    image = models.ImageField(upload_to='arts/gallery')
    def __str__(self):
        return self.image.name


class SportsUpdates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField( default="No data")
    date = models.DateField()
    def __str__(self):
        return self.title

class SportsEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='sports/events')
    def __str__(self):
        return self.title

class SportsTeamStatus(models.Model):
    TEAMS = (("cetus","cetus"),("pegasus","pegasus"),("taurs","taurs"),("lupus","lupus"))
    teamname = models.CharField(max_length=100,choices=TEAMS)
    logo = models.ImageField(upload_to='sports/teams/logos',default='sports/teams/logos/default.png')
    score = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    color = models.CharField(max_length=100,default='red-700')
    image = models.ImageField(upload_to='sports/teams')
    def __str__(self):
        return self.teamname

class SportsGallery(models.Model):
    image = models.ImageField(upload_to='arts/gallery')
    def __str__(self):
        return self.image.name


class NssFaculty(models.Model):
    faculty = models.ManyToManyField(Faculty)


class NssStudents(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nss/students')
    def __str__(self):
        return self.name

class NssGallery(models.Model):
    image = models.ImageField(upload_to='nss/gallery')
    def __str__(self):
        return self.image.name

class NssEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='nss/events')
    def __str__(self):
        return self.title