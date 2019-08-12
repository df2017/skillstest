from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

difficulty_choices = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
)

class Test(models.Model):
    test_name = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20,choices=difficulty_choices, default='easy')
    description = models.TextField(blank=True)
    prueba = models.TextField(blank=True)
    developer_name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'description','prueba','developer_name','create_date')

class ProgramLeng(models.Model):
    language = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.language

class ProgramLengAdmin(admin.ModelAdmin):
    list_display = ('language', 'create_date')

class Solution(models.Model):
    user_dev = models.ForeignKey(User, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(ProgramLeng, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    release_date = models.DateField(auto_now=True)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('user_dev', 'lenguaje','description','release_date')



