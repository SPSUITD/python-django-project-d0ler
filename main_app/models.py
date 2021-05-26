from django.db import models

class PublicChat(models.Model):
  title = models.CharField(max_length=200)

class Message(models.Model):
  author = models.CharField(max_length=200)
  chat = models.CharField(max_length=200)
  text = models.CharField(max_length=1000)
  date_time = models.DateTimeField(auto_now_add=True)
