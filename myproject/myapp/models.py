from django.db import models

# Create your models here.
class state(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    numer_student=models.IntegerField()

    def __str__(self) -> str:
        return self.name

class student(models.Model):
    student_name=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    Marks=models.IntegerField()

    def __str__(self) -> str:
        return self.state