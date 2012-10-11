# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShortURL'
        db.create_table('shorts_shorturl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('shortened_url', self.gf('django.db.models.fields.TextField')(default='[{"original_url": "", "shortened_url": ""}]')),
        ))
        db.send_create_signal('shorts', ['ShortURL'])


    def backwards(self, orm):
        # Deleting model 'ShortURL'
        db.delete_table('shorts_shorturl')


    models = {
        'shorts.shorturl': {
            'Meta': {'object_name': 'ShortURL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortened_url': ('django.db.models.fields.TextField', [], {'default': '\'[{"original_url": "", "shortened_url": ""}]\''}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['shorts']