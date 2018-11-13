from django.db import models

class Abet_Form(models.Model):
     pass



class Application(models.Model):
    program_name = models.TextField(default='')
    street_address = models.TextField(default='')
    city = models.TextField(default='')
    zip = models.TextField(default='')
    contact_person = models.TextField(default='')
    contact_phone = models.TextField(default='')
    contact_email = models.TextField(default='')
    program = models.TextField(default='')
    contact_name = models.TextField(default='')
    po = models.TextField(default='')
    contact_name = models.TextField(default='')
    job_title = models.TextField(default='')
    text = models.TextField(default='')
    abet_form = models.ForeignKey(Abet_Form, default=None)
    so_1 = models.BooleanField(default=False)
