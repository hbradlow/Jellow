# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rating.comments'
        db.add_column('collect_data_rating', 'comments',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rating.comments'
        db.delete_column('collect_data_rating', 'comments')


    models = {
        'collect_data.article': {
            'Meta': {'object_name': 'Article'},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'raw': ('django.db.models.fields.TextField', [], {})
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
        'collect_data.rating': {
            'Meta': {'object_name': 'Rating'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'readability': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'support': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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