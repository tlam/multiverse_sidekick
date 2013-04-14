import os

from django.db import models


def villains_path(instance, filename):
    return os.path.join('images', 'villains', filename)


class Villain(models.Model):
    name = models.CharField(max_length=255)
    starting_hp = models.IntegerField(default=0)
    image = models.ImageField(upload_to=villains_path)

    def __unicode__(self):
        return u'%s' % self.name
