# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hashtag'
        db.create_table('collect_data_hashtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collect_data.Tweet'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('collect_data', ['Hashtag'])

        # Adding field 'Coordinate.tweet'
        db.add_column('collect_data_coordinate', 'tweet',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['collect_data.Tweet']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Hashtag'
        db.delete_table('collect_data_hashtag')

        # Deleting field 'Coordinate.tweet'
        db.delete_column('collect_data_coordinate', 'tweet_id')


    models = {
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
        'collect_data.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['collect_data']