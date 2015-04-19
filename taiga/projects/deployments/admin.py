from django.contrib import admin

# Register your models here.

from . import models

class DeploymentsAdmin(admin.ModelAdmin):

    def get_object(self, *args, **kwargs):
        self.obj = super().get_object(*args, **kwargs)
        return self.obj

admin.site.register(models.Deployment, DeploymentsAdmin)
