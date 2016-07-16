from __future__ import unicode_literals

from django.db import models




class slider(models.Model):
    sliderimage = models.FileField(upload_to="documents/media")
    slidername = models.CharField(max_length=100, null=True, blank=True)
    slidermessage = models.CharField(max_length=100, null=True, blank=True)
    slidercontent = models.TextField(null=True, blank=True)

class comp(models.Model):
    companylogo = models.FileField(upload_to="documents/media", null=True, blank=True)
    companyname = models.CharField(max_length=200, null=True, blank=True)
    companymessage = models.CharField(max_length=300, null=True, blank=True)
    companytext = models.TextField(null=True, blank=True)


class aboutus(models.Model):
    aboutustxt = models.TextField()
    aboutustitle = models.CharField(max_length=100)
    aboutusimage = models.FileField(upload_to="documents/media", null=True, blank=True)



class home(models.Model):
    homeimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    homecontent = models.TextField(null=True, blank=True)
    
    
class logo(models.Model):
    logoimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    logourl = models.CharField(max_length=500, null=True, blank=True)

class services(models.Model):
    servicename = models.CharField(max_length=100, null=True, blank=True)
    serviceimgae = models.FileField(upload_to="documents/media", null=True, blank=True)
    servicecontent = models.TextField( null=True, blank=True)
    
class news(models.Model):
    newsnme = models.CharField(max_length=100, null=True, blank=True)
    newsimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    newscontent = models.TextField( null=True, blank=True)
    newsdate = models.DateField( null=True, blank=True)
    
class promotion(models.Model):
    promotionname = models.CharField(max_length=100, null=True, blank=True)
    promotionimage = models.FileField(upload_to="documents/media", null=True, blank=True)

        
    
class album(models.Model):
    albumname = models.CharField(max_length=100, null=True, blank=True)
    albumimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    albumcontent = models.TextField( null=True, blank=True)
    
class tour(models.Model):
    tourname = models.CharField(max_length=100, null=True, blank=True)
    tourimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    tourcontent = models.TextField( null=True, blank=True)
    tourdate = models.DateField( null=True, blank=True)
    

    
class gallery(models.Model):
    galleryname = models.CharField(max_length=100, null=True, blank=True)
    galleryimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    
class twit(models.Model):
    twitimage = models.FileField(upload_to="documents/media", null=True, blank=True)
    
class video(models.Model):
    videoname = models.CharField(max_length=200, null=True, blank=True)
    videourl = models.CharField(max_length=500)
    
class mail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    content = models.TextField()
    
    
