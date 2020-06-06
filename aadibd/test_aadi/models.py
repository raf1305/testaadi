from django.db import models
from django.urls import reverse
# Create your models here.
class Interview(models.Model):
    Title=models.CharField(max_length=200)
    Date=models.DateField()
class Session(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    Title=models.CharField(max_length=200)
    Date=models.DateField()
    Applicants=models.CharField(max_length=250)
class Applicants(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    Name=models.CharField(max_length=200)