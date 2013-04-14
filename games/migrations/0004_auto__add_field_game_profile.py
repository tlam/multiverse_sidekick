# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.profile'
        db.add_column(u'games_game', 'profile',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['profiles.Profile']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.profile'
        db.delete_column(u'games_game', 'profile_id')


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
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Profile']"}),
            'villain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['villains.Villain']"})
        },
        u'heroes.hero': {
            'Meta': {'object_name': 'Hero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'starting_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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