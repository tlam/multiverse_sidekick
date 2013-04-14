# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.user'
        db.delete_column(u'games_game', 'user_id')


    def backwards(self, orm):
        # Adding field 'Game.user'
        db.add_column(u'games_game', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['auth.User'], unique=True),
                      keep_default=False)


    models = {
        u'environment.environment': {
            'Meta': {'object_name': 'Environment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'games.activehero': {
            'Meta': {'object_name': 'ActiveHero'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['games.Game']"}),
            'hero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['heroes.Hero']"}),
            'hp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'games.game': {
            'Meta': {'object_name': 'Game'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['environment.Environment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'villain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['villains.Villain']"})
        },
        u'heroes.hero': {
            'Meta': {'object_name': 'Hero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'starting_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'villains.villain': {
            'Meta': {'object_name': 'Villain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'starting_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['games']