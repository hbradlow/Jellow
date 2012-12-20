# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paragraph'
        db.create_table('collect_data_paragraph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collect_data.Article'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('collect_data', ['Paragraph'])

        # Adding model 'Article'
        db.create_table('collect_data_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('collect_data', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Paragraph'
        db.delete_table('collect_data_paragraph')

        # Deleting model 'Article'
        db.delete_table('collect_data_article')


    models = {
        'collect_data.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'collect_data.coordinate': {
            'Meta': {'object_name': 'Coordinate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collect_data.Tweet']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'collect_data.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collect_data.Tweet']"})
        },
        'collect_data.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collect_data.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'collect_data.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['collect_data']