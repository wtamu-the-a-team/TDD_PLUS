from django.db import models
import uuid


class User(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #
    # def __str__(self):
    #     return str(self.id)
    pass


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, default=None)
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
    so_1 = models.BooleanField(default=False)
