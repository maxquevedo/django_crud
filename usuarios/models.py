from django.db import models
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_edit', kwargs={'pk': self.pk})