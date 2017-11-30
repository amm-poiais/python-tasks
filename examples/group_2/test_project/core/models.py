# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    user = models.ForeignKey('User', related_name='author')
    tags = models.ManyToManyField('Tag')
    likes = models.ManyToManyField('User', through='MessageLike')


class User(models.Model):
    username=models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return 'Username: %s; email: %s' % (
            self.username, self.email)


class Tag(models.Model):
    text = models.CharField(max_length=16, primary_key=True)


class MessageLike(models.Model):
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()


class Attachment(models.Model):
    content = models.BinaryField()
    message = models.ForeignKey(Message)