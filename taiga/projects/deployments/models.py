from django.db import models

class Deployment(models.Model):
    deployment_server = models.CharField(null=False, blank=True, max_length=256)
    base_git_url = models.CharField(null=False, blank=True, max_length=512)
    base_branch = models.CharField(null=False, blank=True, max_length=128)
    deployment_status = models.BooleanField(default=False)
    #task = models.ForeignKey("tasks.Task")
