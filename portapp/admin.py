from django.contrib import admin

# Register your models here.
from portapp.models import QUESTION,HISTORY,DOOR,DOORFAIL,ACTIVE
# Register your models here.
admin.site.register(QUESTION)
admin.site.register(HISTORY)
admin.site.register(DOOR)
admin.site.register(DOORFAIL)
admin.site.register(ACTIVE)