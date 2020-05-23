from django.db import models

class Youtube(models.Model):
    objects = models.Manager()
    channel=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    prefer=models.IntegerField()
    live=models.BooleanField()
    follower=models.IntegerField()
    link1=models.TextField(blank=True)
    link2=models.TextField(blank=True)
    link3=models.TextField(blank=True)