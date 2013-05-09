# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ParticipationSetting.name'
        db.add_column('participation_participationsetting', 'name', self.gf('django.db.models.fields.CharField')(default='Participation Settings', max_length='30'), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ParticipationSetting.name'
        db.delete_column('participation_participationsetting', 'name')


    models = {
        'participation.participationsetting': {
            'Meta': {'object_name': 'ParticipationSetting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Participation Settings'", 'max_length': "'30'"}),
            'points_100_percent': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'points_50_percent': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'points_75_percent': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'participation.teamparticipation': {
            'Meta': {'ordering': "['-participation']", 'object_name': 'TeamParticipation'},
            'awarded_percent': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'round_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team_mgr.Team']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'team_mgr.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'team_mgr.team': {
            'Meta': {'ordering': "('group', 'name')", 'object_name': 'Team'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['team_mgr.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['participation']
