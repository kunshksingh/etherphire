from os import error
from django.db import models
import sqlite3
# Create your models here.


class Poems(models.Model):
    poem_name = models.CharField(max_length = 128)
    poem = models.CharField(max_length = 8192)
    tags = models.CharField(max_length = 128)
    scrap = models.BooleanField(max_length = 8)
   
    def __str__ (self):
        return self.poem_name
    
class Blog(models.Model):
    title = models.CharField(max_length = 64)
    text = models.CharField(max_length = 8192)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    
    