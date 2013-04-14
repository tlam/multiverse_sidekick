from django.conf import settings
from django.db import models


class Game(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL)
    villain = models.ForeignKey('villains.Villain')
    villain_hp = models.IntegerField(default=0)
    environment = models.ForeignKey('environment.Environment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Game %s' % self.profile


class ActiveHero(models.Model):
    hero = models.ForeignKey('heroes.Hero')
    game = models.ForeignKey('games.Game')
    hp = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.hero
