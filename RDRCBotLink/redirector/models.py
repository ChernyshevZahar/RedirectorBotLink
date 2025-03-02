from django.db import models

class LinkBase(models.Model):
    name = models.CharField(max_length=100)
    getlink = models.CharField(max_length=100)
    postLink =  models.CharField(max_length=100)


