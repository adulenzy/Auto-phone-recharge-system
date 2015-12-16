# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Carrier.company'
        db.delete_column(u'core_carrier', 'company_id')


        # Changing field 'Carrier.recharge_number'
        db.alter_column(u'core_carrier', 'recharge_number', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'Carrier.admin_site'
        db.alter_column(u'core_carrier', 'admin_site', self.gf('django.db.models.fields.CharField')(default='', max_length=500))
        # Deleting field 'Plan.company'
        db.delete_column(u'core_plan', 'company_id')


        # Changing field 'Plan.plan_id'
        db.alter_column(u'core_plan', 'plan_id', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Plan.api_id'
        db.alter_column(u'core_plan', 'api_id', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'Plan.sc_sku'
        db.alter_column(u'core_plan', 'sc_sku', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

    def backwards(self, orm):
        # Adding field 'Carrier.company'
        db.add_column(u'core_carrier', 'company',
                      self.gf('ppars.apps.core.fields.BigForeignKey')(to=orm['core.CompanyProfile'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Carrier.recharge_number'
        db.alter_column(u'core_carrier', 'recharge_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Carrier.admin_site'
        db.alter_column(u'core_carrier', 'admin_site', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))
        # Adding field 'Plan.company'
        db.add_column(u'core_plan', 'company',
                      self.gf('ppars.apps.core.fields.BigForeignKey')(to=orm['core.CompanyProfile'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Plan.plan_id'
        db.alter_column(u'core_plan', 'plan_id', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Plan.api_id'
        db.alter_column(u'core_plan', 'api_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Plan.sc_sku'
        db.alter_column(u'core_plan', 'sc_sku', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.autorefill': {
            'Meta': {'object_name': 'AutoRefill'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('ppars.apps.core.fields.BigForeignKey', [], {'related_name': "'autorefill'", 'to': u"orm['core.Customer']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'last_renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_renewal_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'need_buy_pins': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_buy_pins_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'plan': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Plan']"}),
            'pre_refill_sms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pre_refill_sms_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'refill_type': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '2'}),
            'renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'renewal_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'renewal_interval': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'default': "'MN'", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'send_bought_pins': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trigger': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        u'core.captchalogs': {
            'Meta': {'object_name': 'CaptchaLogs'},
            'carrier': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Carrier']", 'null': 'True', 'blank': 'True'}),
            'carrier_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Customer']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'plan': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Plan']", 'null': 'True', 'blank': 'True'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'refill_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'transaction': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Transaction']", 'null': 'True', 'blank': 'True'}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'core.carrier': {
            'Meta': {'object_name': 'Carrier'},
            'admin_site': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_time': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recharge_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'renew_days': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'renew_months': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.carrieradmin': {
            'Meta': {'object_name': 'CarrierAdmin'},
            'carrier': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Carrier']"}),
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.commandlog': {
            'Meta': {'object_name': 'CommandLog'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        u'core.companyprofile': {
            'Meta': {'object_name': 'CompanyProfile'},
            'able_change_send_pin_prerefill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'asana_api_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'asana_project_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'asana_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'asana_workspace': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'authorize_api_login_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'authorize_precharge_days': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'authorize_transaction_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'auto_changing_payment_processing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'block_duplicate_phone_number': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'block_duplicate_schedule': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cccharge_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'date_limit_license_expiries': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deathbycaptcha_count': ('django.db.models.fields.IntegerField', [], {'default': '5000', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'deathbycaptcha_current_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'deathbycaptcha_email_balance': ('django.db.models.fields.IntegerField', [], {'default': '70', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'deathbycaptcha_emailed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'deathbycaptcha_pass': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'deathbycaptcha_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'default_zip': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'deposit_amount_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dollar_pass': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dollar_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dollar_user': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'insufficient_funds_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'license_expiries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'long_retry_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'long_retry_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mandrill_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'mandrill_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'pageplus_refillmethod': ('django.db.models.fields.CharField', [], {'default': "'TW'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'pin_error': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'precharge_failed_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'precharge_notification_type': ('django.db.models.fields.CharField', [], {'default': "'SE'", 'max_length': '2', 'blank': 'True'}),
            'sales_agent_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'sc_company_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sc_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'sc_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'schedule_limit': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'send_pin_prerefill': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'send_status': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'short_retry_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'short_retry_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_updates': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'superuser_profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '7', 'decimal_places': '4'}),
            'twilio_auth_token': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'twilio_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'twilio_sid': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'unused_charge_notification': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'usaepay_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'usaepay_pin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'usaepay_source_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'usaepay_username': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'use_asana': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_sellercloud': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.confirmdp': {
            'Meta': {'object_name': 'ConfirmDP'},
            'confirm': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'authorize_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'charge_getaway': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'charge_type': ('django.db.models.fields.CharField', [], {'default': "'CA'", 'max_length': '2'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creditcard': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'customer_discount': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'email_success_charge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_success_refill': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'group_sms': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'precharge_sms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'primary_email_lowercase': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'sc_account': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'selling_price_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['price.SellingPriceLevel']"}),
            'send_pin_prerefill': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'send_status': ('django.db.models.fields.CharField', [], {'default': "'NO'", 'max_length': '2'}),
            'sms_email': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '500', 'blank': 'True'}),
            'sms_gateway': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['notification.SmsEmailGateway']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'taxable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'usaepay_custid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'usaepay_customer_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'core.importlog': {
            'Meta': {'object_name': 'ImportLog'},
            'command': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        u'core.log': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Log'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'core.news': {
            'Meta': {'object_name': 'News'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'core.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']"}),
            'customer': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Customer']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'core.pinreport': {
            'Meta': {'object_name': 'PinReport'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '3'})
        },
        u'core.plan': {
            'Meta': {'object_name': 'Plan'},
            'api_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'carrier': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Carrier']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'plan_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'plan_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plan_type': ('django.db.models.fields.CharField', [], {'default': "'PI'", 'max_length': '2'}),
            'sc_sku': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'universal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'universal_plan': ('ppars.apps.core.fields.BigForeignKey', [], {'blank': 'True', 'related_name': "'plan'", 'null': 'True', 'to': u"orm['core.Plan']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.plandiscount': {
            'Meta': {'object_name': 'PlanDiscount'},
            'carrier': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Carrier']"}),
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'plan': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Plan']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'adv_status': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'autorefill': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.AutoRefill']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'bought_pins': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bought_pins_retry_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'bought_pins_retry_count_err_token': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'create_asana_ticket': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'current_step': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'customer_confirmation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'customer_str': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'get_pin_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_paid': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number_str': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'pin_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'plan_str': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'profit': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'refill_type_str': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'retry_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'retry_interval': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'sellercloud_note_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sellercloud_order_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sellercloud_payment_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'trigger': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'triggered_by': ('django.db.models.fields.CharField', [], {'default': "'System'", 'max_length': '128'}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        u'core.transactioncreatedfromto': {
            'Meta': {'object_name': 'TransactionCreatedFromTo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction_from': ('ppars.apps.core.fields.BigForeignKey', [], {'related_name': "'original_transaction'", 'to': u"orm['core.Transaction']"}),
            'transaction_to': ('ppars.apps.core.fields.BigForeignKey', [], {'related_name': "'similar_transaction'", 'to': u"orm['core.Transaction']"})
        },
        u'core.transactionerror': {
            'Meta': {'object_name': 'TransactionError'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'transaction': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Transaction']"})
        },
        u'core.transactionstep': {
            'Meta': {'object_name': 'TransactionStep'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'adv_status': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'transaction': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Transaction']"})
        },
        u'core.unusedpin': {
            'Meta': {'object_name': 'UnusedPin'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.CompanyProfile']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'plan': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Plan']"}),
            'transaction': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['core.Transaction']", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('ppars.apps.core.fields.BigForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'company': ('ppars.apps.core.fields.BigForeignKey', [], {'blank': 'True', 'related_name': "'user_profile'", 'null': 'True', 'to': u"orm['core.CompanyProfile']"}),
            'id': ('ppars.apps.core.fields.BigAutoField', [], {'primary_key': 'True'}),
            'profit_restriction': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'superuser_profile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'updates_email': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('ppars.apps.core.fields.BigOneToOneField', [], {'blank': 'True', 'related_name': "'profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'notification.smsemailgateway': {
            'Meta': {'object_name': 'SmsEmailGateway'},
            'gateway': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'price.sellingpricelevel': {
            'Meta': {'object_name': 'SellingPriceLevel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']