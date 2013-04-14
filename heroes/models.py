import os

from django.db import models


def heroes_path(instance, filename):
    return os.path.join('images', 'heroes', filename)


class Hero(models.Model):
    name = models.CharField(max_length=255)
    starting_hp = models.IntegerField(default=0)
    image = models.ImageField(upload_to=heroes_path)

    def __unicode__(self):
        return u'%s' % self.name

    @staticmethod
    def choices():
        hero_tuples = ()
        for hero in Hero.objects.all():
            hero_tuples = hero_tuples + ((hero.id, hero.name),)
        return hero_tuples
