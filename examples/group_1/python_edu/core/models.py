# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Group(models.Model):
    number = models.CharField(max_length=16)
    course = models.IntegerField()


class Student(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=24)
    group = models.ForeignKey(Group)
    labs = models.ManyToManyField('Task', through='StudentTask')


class Teacher(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=24)


class Subject(models.Model):
    name = models.CharField(max_length=64, unique=True)
    teacher = models.ForeignKey(Teacher)



class Task(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    subject = models.ForeignKey(Subject)

class StudentTask(models.Model):
    assignment_date = models.DateTimeField()
    student = models.ForeignKey(Student)
    task = models.ForeignKey(Task)
    status = models.CharField(max_length=16)