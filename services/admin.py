from django.contrib import admin
from services.models import ContactDetails


class ContactAdmin(admin.ModelAdmin):
    list_display=('fullName','subject','description')

admin.site.register(ContactDetails,ContactAdmin)

# Register your models here.
