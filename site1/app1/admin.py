from django.contrib import admin
from .models import Question,Choice,BenhNhan
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(BenhNhan)