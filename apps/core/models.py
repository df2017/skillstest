from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

difficulty_choices = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20,choices=difficulty_choices, default='easy')
    description = models.TextField(blank=True)
    task = models.TextField(blank=True)
    developer_name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.test_name

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id','test_name','difficulty','description','task','developer_name','create_date')

class ProgramLeng(models.Model):
    leng_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=50, unique=True)
    create_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.language

class ProgramLengAdmin(admin.ModelAdmin):
    list_display = ('leng_id','language', 'create_date')

class Solution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    user_dev = models.ForeignKey(User,on_delete=models.CASCADE)
    leng_program = models.ForeignKey(ProgramLeng, on_delete=models.CASCADE)
    test_choice = models.ForeignKey(Test, on_delete=models.CASCADE)
    description = models.TextField(blank=True )
    release_date = models.DateField(auto_now=True)
    is_done = models.BooleanField(default=False)

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('solution_id','user_dev', 'leng_program','test_choice','description','release_date','is_done')



