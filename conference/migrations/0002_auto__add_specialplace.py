# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SpecialPlace'
        db.create_table('conference_specialplace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
        ))
        db.send_create_signal('conference', ['SpecialPlace'])


    def backwards(self, orm):
        
        # Deleting model 'SpecialPlace'
        db.delete_table('conference_specialplace')


    models = {
        'conference.deadline': {
            'Meta': {'ordering': "['date']", 'object_name': 'Deadline'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'conference.deadlinecontent': {
            'Meta': {'object_name': 'DeadlineContent'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'deadline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Deadline']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'conference.didyouknow': {
            'Meta': {'object_name': 'DidYouKnow'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'conference.event': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Event'},
            'custom': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Schedule']"}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Sponsor']", 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Talk']", 'null': 'True', 'blank': 'True'}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'conference.hotel': {
            'Meta': {'ordering': "['name']", 'object_name': 'Hotel'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'affiliated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'availability': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'conference.mediapartner': {
            'Meta': {'ordering': "['partner']", 'object_name': 'MediaPartner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'partner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'conference.mediapartnerconference': {
            'Meta': {'ordering': "['conference']", 'object_name': 'MediaPartnerConference'},
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.MediaPartner']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'conference.multilingualcontent': {
            'Meta': {'object_name': 'MultilingualContent'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'conference.quote': {
            'Meta': {'ordering': "['conference', 'who']", 'object_name': 'Quote'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'conference.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'conference.speaker': {
            'Meta': {'ordering': "['name']", 'object_name': 'Speaker'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'activity_homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'conference.specialplace': {
            'Meta': {'ordering': "['name']", 'object_name': 'SpecialPlace'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'conference.sponsor': {
            'Meta': {'ordering': "['sponsor']", 'object_name': 'Sponsor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'conference.sponsorincome': {
            'Meta': {'ordering': "['conference']", 'object_name': 'SponsorIncome'},
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Sponsor']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'conference.talk': {
            'Meta': {'ordering': "['title']", 'object_name': 'Talk'},
            'additional_speakers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'additional_speakers'", 'blank': 'True', 'to': "orm['conference.Speaker']"}),
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'slides': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['conference.Speaker']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'video_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'conference.track': {
            'Meta': {'ordering': "['order']", 'object_name': 'Track'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Schedule']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'translate': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['conference']
