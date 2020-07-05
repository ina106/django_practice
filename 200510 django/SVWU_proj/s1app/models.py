from django.db import models

# Create your models here.
    # class Gall(models.Model):
    #     objects = models.Manager()
    #     channel=models.CharField(max_length=50)
    #     name=models.CharField(max_length=50)
    #     prefer=models.IntegerField()
    #     live=models.BooleanField()
    #     follower=models.IntegerField()
    #     link1=models.TextField(blank=True)
    #     link2=models.TextField(blank=True)
    #     link3=models.TextField(blank=True)
    #     #blank=True는 빈칸이어도 오류X
    #     explt=models.TextField(max_length=2000)
    #     summary=models.TextField(max_length=200)
    #     photho=models.ImageField(upload_to="image",blank=True)

class Gall(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="image", null=True)
    date = models.CharField(max_length=10)
    summ = models.CharField(max_length=100)