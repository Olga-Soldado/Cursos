from django.db import models

# Create your models here.
from datetime import date, datetime
from django.utils.dateparse import parse_date
import re
class CursosManager(models.Manager):
    
    def cursos_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "El nombre  debe ser mayor a 5 caracteres"
        if len(postData['description']) < 15:
            errors['description'] = " La descripcion debe ser mayor a 15 caracteres"
        return errors
class Cursos(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    objects = CursosManager()
