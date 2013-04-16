from django.conf import settings
from django.db import models


class Game(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL)
    villain = models.ForeignKey('villains.Villain')
    villain_hp = models.IntegerField(default=0)
    environment = models.ForeignKey('environment.Environment')
    is_over = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Game %s' % self.profile

    def who_won(self):
        if self.is_over:
            if self.villain_hp:
                return 'Villain'
            else:
                return 'Hero'
        return 'In progress'


class ActiveHero(models.Model):
    hero = models.ForeignKey('heroes.Hero')
    game = models.ForeignKey('games.Game')
    hp = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.hero
