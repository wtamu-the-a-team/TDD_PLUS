from django.db import models
import uuid


class User(models.Model):
    uuid_id = models.UUIDField(default=uuid.uuid4, editable=False)


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
    job_title = models.TextField(default='')
    text = models.TextField(default='')
    so_1 = models.BooleanField(default=False)

    def is_equal(self, application):
        if self.id != application.id:
            return False
        if self.user != application.user:
            return False
        if self.program_name != application.program_name:
            return False
        if self.street_address != application.street_address:
            return False
        if self.city != application.city:
            return False
        if self.zip != application.zip:
            return False
        if self.contact_person != application.contact_person:
            return False
        if self.contact_phone != application.contact_phone:
            return False
        if self.contact_email != application.contact_email:
            return False
        if self.program != application.program:
            return False
        if self.contact_name != application.contact_name:
            return False
        if self.po != application.po:
            return False
        if self.job_title != application.job_title:
            return False
        if self.text != application.text:
            return False
        if self.so_1 != application.so_1:
            return False
        return True
