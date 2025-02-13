from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrganizationMembership(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)
    owner = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.organization.name}" 