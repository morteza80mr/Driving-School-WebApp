from multiprocessing import context
from tkinter import CASCADE
from unicodedata import name
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from extensions.utils import jalali_converter

# Create your models here.
class User(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('R','Registry_man'),
        ('C','Class_man'),
        ('F','Financial_man'),
        ('T','Trainer'),
        ('S','Student'),
        ('M','Manager')
    ]
    username = models.CharField(max_length=10,primary_key=True)
    first_name_user = models.CharField (max_length=60)
    family_name_user = models.CharField (max_length=120)
    National_ID_user = models.CharField(max_length=10)
    User_role = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES)
    

class Employee (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Student (models.Model):
    LITERATE_CHOICES = [
        ('L','Literate'),
        ('I','Illiterate'),
    ]
    father_name_Student = models.CharField (max_length=60)
    Address_Student = models.CharField (max_length=512)
    Zip_code_Student = models.CharField (max_length=24)
    Literate = models.CharField(max_length=1,choices=LITERATE_CHOICES)
    Birthday = models. DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def j_Birthday(self):
        return jalali_converter(self.Birthday)

class Document (models.Model):
    CATCHED_CHOICES = [
        ('C','Catched'),
        ('N','Not_Catched'),
    ]
    Registry_man_ID = models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='+')
    Student_ID = models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='+')
    Catched = models.CharField(max_length=1,choices=CATCHED_CHOICES,default='N')
    Date_catched = models.DateField(auto_now=True)

class Tuition (models.Model):
    Financial_man_ID = models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='+')
    Student_ID = models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='+')
    Time_recived = models.TimeField(auto_now=True)
    Date_recived = models.DateField(auto_now=True)
    Price=models.BigIntegerField()

class classroom (models.Model):
    TYPE_EXAM = [
        ('T','Theory'),
        ('I','In_Practice'),
    ]
    TIME_CLASS = [
        ('14-16','14-16'),
        ('16-18','16-18'),
        ('18-20','18-20')
    ]
    Date_class = models.DateField()
    Time_class = models.CharField(max_length=5,choices=TIME_CLASS)
    ID_of_students = models.ManyToManyField('User' ,related_name='+',through='status')
    ID_of_Trainer = models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='+')
    name_of_Trainer = models.CharField(max_length=180)
    type_of_class = models.CharField(max_length=1,choices=TYPE_EXAM)
    creator_of_class_ID = models.ForeignKey( 'User' ,on_delete=models.CASCADE,related_name='+')
    Capacity = models.IntegerField()

    def j_Date_class(self):
        return jalali_converter(self.Date_class)

class status(models.Model):
        student = models.ForeignKey('User',on_delete=models.CASCADE)
        classroom = models.ForeignKey('Classroom',on_delete=models.CASCADE)

        class Meta:
            unique_together = [['student','classroom']]