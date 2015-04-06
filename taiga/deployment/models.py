from django.db import models

# Create your models here.


class Deployment(models.Model):
    server = models.CharField(max_length=30)
    base_git_url = models.CharField(max_length=30)
    base_branch = models.CharField(max_length=30)
    deployment_status = models.CharField(max_length=30)
