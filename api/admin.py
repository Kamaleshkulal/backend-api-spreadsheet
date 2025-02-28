from django.contrib import admin

# Register your models here.
from .models import Spreadsheet, Cell
admin.site.register(Spreadsheet)
admin.site.register(Cell)