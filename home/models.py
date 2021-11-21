# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StMonthlyStatistic(models.Model):
    month = models.CharField(max_length=50)
    year = models.IntegerField()
    total_calls = models.IntegerField()
    answered_calls = models.IntegerField()
    response_time = models.IntegerField()
    service_level = models.IntegerField()
    abandonment_rate = models.IntegerField()
    queu_name = models.CharField(max_length=10, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'st_monthly_statistic'


class Test(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test'
