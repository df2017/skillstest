from django.contrib import admin
from .models import Test, TestAdmin, ProgramLeng,ProgramLengAdmin,Solution,SolutionAdmin

admin.site.register(Test,TestAdmin)
admin.site.register(ProgramLeng,ProgramLengAdmin)
admin.site.register(Solution,SolutionAdmin)

