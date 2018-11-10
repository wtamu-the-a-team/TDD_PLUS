from django.db import models

class Abet_Form(models.Model):
    pass


class Application(models.Model):
    program_name = models.TextField(default='')
    po = models.TextField(default='')
    contact_name = models.TextField(default='')
    job_title = models.TextField(default='')
    text = models.TextField(default='')
    list = models.ForeignKey(Abet_Form, default=None)
    so_1 = models.BooleanField(default=False)
