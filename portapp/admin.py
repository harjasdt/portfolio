from django.contrib import admin

# Register your models here.
from portapp.models import QUESTION,HISTORY
# Register your models here.
admin.site.register(QUESTION)
admin.site.register(HISTORY)