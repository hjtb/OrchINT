from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField()
    date_registered = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return str(self.admin_id)


class Channel(models.Model):
    channel_id = models.IntegerField()
    channel_code_name = models.CharField(max_length=24)
    admin_id = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    region = models.CharField(max_length=24)


class Commander(models.Model):
    channel_id = models.IntegerField()
    commander_id = models.IntegerField()
    commander_code_name = models.CharField(max_length=24, null=True, blank=True)
    password = models.CharField(max_length=16)
    donations = models.IntegerField()
    admin = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)


class Source(models.Model):
    commander_id = models.IntegerField()
    qr_code = models.IntegerField()
    source_id = models.IntegerField()
    code_name = models.CharField(max_length=24, null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True)
    reputation = models.IntegerField()
    locale = models.CharField(max_length=24)
    password = models.CharField(max_length=16)
    donations = models.IntegerField()
    qr_code_status = models.BooleanField()


class IntelItem(models.Model):
    source_id = models.IntegerField()
    item_id = models.IntegerField()
    title = models.CharField(max_length=24)
    summary = models.TextField(max_length=400, null=True, blank=True)
    media_id = models.IntegerField()
    time_added = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    urgency = models.CharField(max_length=24)


class QrCode(models.Model):
    commander_id = models.IntegerField()
    qr_code = models.URLField()
    date_of_issue = models.DateField(auto_now_add=True)
    url_count_hit = models.IntegerField()


class Media(models.Model):
    media_id = models.IntegerField()
    media_url = models.URLField()
    date_created = models.DateField(auto_now_add=True)
