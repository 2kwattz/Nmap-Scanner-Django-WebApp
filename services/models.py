from django.db import models

class ContactDetails(models.Model):
    fullName = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=50,null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=False)

class UserDetails(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False, verbose_name="First Name")
    lastName = models.CharField(max_length=50, null=False, blank=False, verbose_name="Last Name")
    emailAddress = models.EmailField(unique=True, verbose_name="Email Address")
    user_created_datetime = models.DateTimeField(auto_now=True)
