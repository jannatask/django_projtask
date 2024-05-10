from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField
    age = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    students = models.ManyToManyField(Students)

def __str__(self):
    return self.title