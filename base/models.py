from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField()
    password = models.CharField(min_length=8, max_length=16)


class Channel(models.Model):
    channel_id = models.IntegerField()
    admin_id = models.IntegerField()
    region = models.CharField(min_length=3, max_length=24)


class Commander(models.Model):
    channel_id = models.IntegerField()
    commander_id = models.IntegerField()
    commander_name = models.CharField(min_length=3, max_length=24)
    password = models.CharField(min_length=8, max_length=16)
    donations = models.IntegerField()
    admin = models.BooleanField(default=False)


class Source(models.Model):
    commander_id = models.IntegerField()
    qr_code = models.IntegerField()
    source_id = models.IntegerField()
    code_name = models.CharField(min_length=3, max_length=24)
    date_registered = models.DateField()
    reputation = models.IntegerField()
    locale = models.CharField(min_length=3, max_length=24)
    password = models.CharField(min_length=8, max_length=16)
    donations = models.IntegerField()
    qr_code_status = models.BooleanField()


class IntelItem(models.Model):
    source_id = models.IntegerField()
    item_id = models.IntegerField()
    title = models.CharField(min_length=3, max_length=24)
    summary = models.CharField(min_length=3, max_length=400)
    media_id = models.integerField()
    time = models.DateTimeField()
    verified = models.booleanField(default=False)
    urgency = models.CharField()


class QrCode(models.Model):
    commander_id = models.IntegerField()
    qr_code = models.URLField()
    date_of_issue = models.DateField()
    url_count_hit = models.IntegerField()


class Media(models.Model):
    media_id = models.IntegerField()
    media_url = models.URLField()
