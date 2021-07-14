from django.contrib import admin
from .models import  ContactTeam
from django.utils.html import  format_html

# Register your models here.
class ContactTeamAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'email', 'company_name', 'subject')
    list_display_links = ('full_name', 'email', 'company_name', 'subject')

admin.site.register(ContactTeam, ContactTeamAdmin)