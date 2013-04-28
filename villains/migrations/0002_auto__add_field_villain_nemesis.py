# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Villain.nemesis'
        db.add_column(u'villains_villain', 'nemesis',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['heroes.Hero'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Villain.nemesis'
        db.delete_column(u'villains_villain', 'nemesis_id')


    models = {
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
            'nemesis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['heroes.Hero']", 'null': 'True', 'blank': 'True'}),
            'starting_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['villains']