# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import random

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
# Create your views here.

def hello(request):
    response = HttpResponse('Hello, world!')
    return response


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers_list.html', {
        'teachers': teachers
    })


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {
        'subjects': subjects
    })

def subject_details(request):
    subject_id = request.GET['id']
    subject = Subject.objects.get(pk=subject_id)
    subject_tasks = Task.objects.filter(subject=subject)
    return render(
        request,
        'subject_details.html',
        {
            'subject': subject,
            'subject_tasks': subject_tasks
        }
    )

def add_solution(request):
    if request.method == 'GET':
        print('IT WAS GET!!!!')
        return render(
            request,
            'add_solution.html',
            {
            }
        )
    else:
        student = Student.objects.first()
        task_id = request.GET['id']
        task = Task.objects.get(pk=task_id)
        solution_check = random.randint(0, 5)
        if solution_check == 0:
            status='completed'
            message = 'Your task is finished'
        else:
            status='failed'
            message = 'Your task is failed'

        try:
            student_task = StudentTask.objects.get(
                    student=student, task=task)
            print('exist')
        except StudentTask.DoesNotExist:
            print('not_exist')
            student_task = StudentTask.objects.create(
                    student=student,
                    task=task,
                assignment_date=datetime.datetime.now())
        finally:
            student_task.status=status
            student_task.save()


        return render(
            request,
            'add_solution.html',
            {
                'message': message
            }
        )

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput)

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return HttpResponse('Login complete!')
            else:
                return render(
                    request,
                    'login_form.html',
                    {login_form: login_form})
    else:
        form = LoginForm()
        return render(
            request,
            'login_form.html',
            {'login_form': form})

def main(request):
    return render(request, 'main.html')