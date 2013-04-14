from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.OneToOneField(User)
    villain = models.ForeignKey('villains.Villain')
    environment = models.ForeignKey('environment.Environment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Game %s' % self.user


class ActiveHero(models.Model):
    hero = models.ForeignKey('heroes.Hero')
    game = models.ForeignKey('games.Game')
    hp = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.hero
