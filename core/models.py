from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        blank=True, null=True, upload_to='static/assets/user')
    phone = models.CharField(max_length=255, blank=True, null=True)
