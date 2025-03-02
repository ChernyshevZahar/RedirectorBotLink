from django.db import models

class LinkBase(models.Model):
    name = models.CharField(max_length=100)
    getlink = models.CharField(max_length=100)
    postLink =  models.CharField(max_length=100)


class utmBase(models.Model):
    unicKye = models.CharField(max_length=100)
    utms = models.CharField(max_length=500, null=True, blank=True )
    linkbase = models.ManyToManyField(LinkBase, related_name='links')