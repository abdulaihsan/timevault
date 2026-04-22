# from django.contrib import admin
# Register your models here.
# from .models import VaultLetter
# admin.site.register(VaultLetter)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import VaultLetter

@admin.register(VaultLetter)
class VaultLetterAdmin(ImportExportModelAdmin):
    pass
