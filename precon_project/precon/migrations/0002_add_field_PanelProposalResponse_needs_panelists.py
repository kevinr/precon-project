# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PanelProposal.needs_panelists'
        db.add_column(u'precon_panelproposal', 'needs_panelists',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PanelProposal.needs_panelists'
        db.delete_column(u'precon_panelproposal', 'needs_panelists')


    models = {
        u'precon.panel': {
            'Meta': {'object_name': 'Panel'},
            'blurb': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'precon.panelproposal': {
            'Meta': {'object_name': 'PanelProposal'},
            'blurb': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'needs_panelists': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'precon.panelproposalresponse': {
            'Meta': {'object_name': 'PanelProposalResponse'},
            'attending_interest': ('django.db.models.fields.CharField', [], {'default': "'not interested'", 'max_length': '50'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'panel_proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['precon.PanelProposal']"}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['precon.Participant']"}),
            'presenting_interest': ('django.db.models.fields.CharField', [], {'default': "'not interested'", 'max_length': '50'})
        },
        u'precon.participant': {
            'Meta': {'object_name': 'Participant'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nonce': ('django.db.models.fields.CharField', [], {'default': "'qg3gip'", 'unique': 'True', 'max_length': '6'}),
            'panel_proposals_responded': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'participants_responded'", 'blank': 'True', 'through': u"orm['precon.PanelProposalResponse']", 'to': u"orm['precon.PanelProposal']"}),
            'panels': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'panelists'", 'blank': 'True', 'to': u"orm['precon.Panel']"})
        }
    }

    complete_apps = ['precon']