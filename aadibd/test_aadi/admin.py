from django.contrib import admin

# Register your models here.
from .models import Interview,Session,Applicants
admin.site.register(Interview)
admin.site.register(Session)
admin.site.register(Applicants)