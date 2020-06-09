from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class permission(models.Model):
    permissiontype = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.permissiontype


class role(models.Model):
    rolename = models.CharField(max_length=200, null=True, blank=True)
    permissions = models.ManyToManyField(permission, blank=True)

    def __str__(self):
        return self.rolename


class profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    head = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_head')
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    roles = models.ManyToManyField(role, blank=True)

    def __str__(self):
        return str(self.user)
