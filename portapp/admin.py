from django.contrib import admin

# Register your models here.
from portapp.models import QUESTION,HISTORY,DOOR,DOORFAIL,ACTIVE,TEMP
from import_export.admin import ExportActionMixin

# Register your models here.
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('temp','ph','mos','n','p','k','time')
# Register your models here.
admin.site.register(QUESTION,BookAdmin)
admin.site.register(HISTORY)
admin.site.register(DOOR)
admin.site.register(DOORFAIL)
admin.site.register(ACTIVE)
admin.site.register(TEMP)