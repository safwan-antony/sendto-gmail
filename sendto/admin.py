from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Sendto
# Register your models here.
@admin.register(Sendto)
class SendtoAdmin(ImportExportModelAdmin):
    pass
