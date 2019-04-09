from django.contrib import admin
from .models import Information, Specialty, Discipline, Question


admin.site.register(Information)
admin.site.register(Specialty)
admin.site.register(Discipline)

admin.site.register(Question)
