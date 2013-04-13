import os

from django.db import models


def environment_path(instance, filename):
    return os.path.join('images', 'environment', filename)


class Environment(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=environment_path)

    def __unicode__(self):
        return u'%s' % self.name
