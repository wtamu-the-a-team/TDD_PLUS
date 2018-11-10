from django.db import models

class Abet_Form(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(Abet_Form, default=None)

