
from django.contrib import admin

# Register your models here.
from libro.models import CodeBook, Usuario, Task

class TaskAdmin(admin.ModelAdmin):
    #readonly_fields: ("created", )
    pass

admin.site.register(CodeBook)
admin.site.register(Usuario)
admin.site.register(Task, TaskAdmin)

        