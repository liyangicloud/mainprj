# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CIDAccessRecordManager(models.Manager):
    def get_queryset(self):
        return super(CIDAccessRecordManager,self).get_queryset().filter(isDeleteFlag=False)

class CIDAccessRecord(models.Model):
    class Meta:
        db_table = "cidaccessrecord"

    objEx = CIDAccessRecordManager()
    ipAdd = models.CharField(max_length=128)
    CID = models.CharField(max_length=128)
    isDeleteFlag = models.BooleanField(default=False)
    timeStamp = models.DateTimeField()


class fileDownloadLog(models.Model):
    CID = models.CharField(max_length=128)
    timeStamp = models.DateTimeField()
