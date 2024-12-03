from django.db import models

class ContactDetails(models.Model):
    full_name = models.CharField(max_length=50),null=False, blank=False
    subject = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField()
    email = models.CharField(max_length=40,null=False, blank=False)
