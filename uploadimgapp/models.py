from django.db import models

# Create your models here.
class profile(models.Model):
    def namefile(instance, filename):
        return '/'.join(['images', str(instance.name), filename])

    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to = namefile, blank=True)
