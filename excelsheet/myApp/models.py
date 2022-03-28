from django.db import models

class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    login_id = models.EmailField(blank=True)
    #birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)