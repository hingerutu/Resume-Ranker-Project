from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=240)
    doc = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year =  models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    email = models.EmailField(null=True)
    CGPA = models.FloatField(default=7,validators=[MinValueValidator(0), MaxValueValidator(10)])
    score = models.IntegerField(default=0)
 

    def __str__(self):
        return f'{self.Name} - {self.email}'
    


class Pyresume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=240)
    doc = models.FileField(upload_to='resumes/', blank=True, null=True)
    year =  models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    email = models.EmailField(null=True)
    CGPA = models.FloatField(default=7,validators=[MinValueValidator(0), MaxValueValidator(10)])
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.Name} - {self.email}'