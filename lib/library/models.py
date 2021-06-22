from django.db import models


class Category(models.Model):
    name = models.CharField()


class Author(models.Model):
    name = models.CharField()
    url_description = models.URLField()


class Translator(models.Model):
    name = models.CharField()
    url_description = models.URLField()


class Publisher(models.Model):
    name = models.CharField()
    url_description = models.URLField()

# class suitable_age in user model
# class statuc

class Book(models.Model):
    #user =          models.ForeignKey()
    #category =      models.ForeignKey()
    #author =        models.ForeignKey()
    #translator =    models.ForeignKey()
    #suitable_age =  models.ForeignKey()
    title =         models.CharField()
    page_number =   models.PositiveIntegerField()
    isbn =          models.PositiveBigIntegerField()
    pic =           models.ImageField()
    description =   models.TextField()
    created =       models.DateTimeField()
    updated =       models.DateTimeField()
    
