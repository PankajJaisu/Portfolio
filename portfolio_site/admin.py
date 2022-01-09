from django.contrib import admin
from .models import my_profile,my_education,certification,my_experience,Blog,Project,Skill
# Register your models here.
admin.site.register(my_profile)
admin.site.register(my_education)
admin.site.register(certification)
admin.site.register(my_experience)
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Skill)
