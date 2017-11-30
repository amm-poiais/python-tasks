# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login


from core.models import User, Message, Tag
# Create your views here.


def hello(request):
    return HttpResponse('Hello, World!')


def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def user_profile(request):
    user_id = request.GET['user_id']
    user = User.objects.get(pk=user_id)
    user_messages = Message.objects.filter(
        user=user).order_by('-id')
    user_messages = user_messages[:10]
    user_messages = [
        {
            'text': user_message.text,
            'timestamp': user_message.timestamp,
            'likes_number': user_message.likes.count()
        }
        for user_message in user_messages
    ]
    return render(
        request,
        'user_details.html',
        {'user': user,
         'user_messages': user_messages})

def main(request):
    tags = Tag.objects.all()
    return render(request, 'main.html', {'tags': tags})

def post_message(request):
    if request.method == 'POST':
        print(request.POST)
        message = request.POST['message']
        tag_list = request.POST.get('tags')
        print('Tag list', tag_list)
        # dirty hack to get user
        user = User.objects.first()

        message = Message.objects.create(
            text=message,
            timestamp=datetime.datetime.now(),
            user=user)

        for tag in tag_list:
            print('Tag is: ' + tag)
            tag_item = Tag.objects.get(text=tag)
            message.tags.add(tag_item)
        return HttpResponse('ok')

class LoginForm(forms.Form):
    login = forms.CharField(required=True, min_length=8)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data['login'],
                password=login_form.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                return HttpResponse('Login ok!')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {
        'login_form': login_form})


def check_user(request):
    return HttpResponse(str(request.user))

def base_template(request):
    return render(request, 'base.html')