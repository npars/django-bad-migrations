from django.db import models


class RenamedModel(models.Model):
    pass


class AnotherModel(models.Model):
    foreign_key_field = models.ForeignKey(RenamedModel)
