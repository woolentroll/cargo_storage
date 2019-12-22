from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone


class Operation(models.Model):
    operation_type = models.IntegerField('Тип операции', default=0)
    status = models.IntegerField('Статус', default=0)
    date_created = models.DateTimeField('date created', default=datetime.now)
    description = models.CharField(max_length=200)
    user_created = models.ForeignKey(User, null=True, blank=True, related_name='operations',
                                     verbose_name='Пользователь создавший операцию',
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return "Operation: {}, created: {}, description: {}".format(self.pk, self.date_created, self.description)


class Document(models.Model):
    doc_type = models.IntegerField('Тип документа', default=0)
    date_created = models.DateTimeField('date created', default=datetime.now)
    doc_number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    operation = models.ForeignKey(Operation, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name='documents')

    def __str__(self):
        return "Document: {}, created: {}, description: {}".format(self.pk, self.date_created, self.description)


class Item(models.Model):
    date_created = models.DateTimeField('date created', default=datetime.now)
    description = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=60)
    weight = models.IntegerField('Вес', default=0)
    factory_number = models.CharField(max_length=60, default="")
    passport_number = models.CharField(max_length=60, default="")

    def __str__(self):
        return "Item {}, created: {}, description: {}".format(self.pk, self.date_created, self.description)


class ItemEntry(models.Model):
    date_created = models.DateTimeField('date created', default=datetime.now)
    description = models.CharField(max_length=200)
    operation = models.ForeignKey(Operation, null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name='entries')
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name='entries')

    def __str__(self):
        return "ItemEntry {}, created: {}, description: {}".format(self.pk, self.date_created, self.description)


class UserProfile(User):
    date_created = models.DateTimeField('date created', default=datetime.now)
    full_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "UserProfile {}, created: {}, full_name: {}".format(self.pk, self.date_created, self.full_name)
