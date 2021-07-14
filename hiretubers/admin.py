from django.contrib import admin
from .models import Hiretuber
from django.utils.html import  format_html
# Register your models here.

class HtAdmin(admin.ModelAdmin):

    list_display = ('id', 'first_name', 'email', 'tuber_name')
    

admin.site.register(Hiretuber, HtAdmin)