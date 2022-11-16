

from email.policy import default
from django.db import models
from adminpanel.models import User
from adminpanel.models import designation




class Interview(models.Model):
    name = models.CharField(max_length = 200)
    domain = models.CharField(max_length=20, choices=designation)
   
   
    datetime = models.DateTimeField(auto_now_add=False, auto_now=False)
    interviewer = models.ForeignKey(User, on_delete = models.CASCADE)

    is_delete = models.BooleanField(default=False)
    attempt = models.IntegerField(default=0)
    cv = models.ImageField(upload_to="static/images")


    


class Meeting(models.Model):
    agenda = models.CharField(max_length =200)
    description = models.TextField()
    withs = models.ManyToManyField(User)
    date_time = models.DateTimeField(auto_now_add=False, auto_now = False)
    

    