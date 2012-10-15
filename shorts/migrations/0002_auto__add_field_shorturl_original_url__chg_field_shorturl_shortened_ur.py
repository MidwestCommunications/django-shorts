# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ShortURL.original_url'
        db.add_column('shorts_shorturl', 'original_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)


        # Changing field 'ShortURL.shortened_url'
        db.alter_column('shorts_shorturl', 'shortened_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):
        # Deleting field 'ShortURL.original_url'
        db.delete_column('shorts_shorturl', 'original_url')


        # Changing field 'ShortURL.shortened_url'
        db.alter_column('shorts_shorturl', 'shortened_url', self.gf('django.db.models.fields.TextField')())

    models = {
        'shorts.shorturl': {
            'Meta': {'object_name': 'ShortURL'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'shortened_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
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