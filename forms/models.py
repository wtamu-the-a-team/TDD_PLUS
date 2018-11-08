from django.db import models

class Form(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    form = models.ForeignKey(Form, default=None)
# Create your models here test- resume at "A New Field Means a New Migration".
