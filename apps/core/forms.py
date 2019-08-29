from django.forms import ModelForm
from django import forms
from .models import Solution, Test
from ckeditor.widgets import CKEditorWidget

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['test_id','test_name','difficulty','description','task']

class SolutionForm(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Solution
        fields = ['leng_program','test_choice','description','is_done','create_date']

    def __init__(self, user_dev, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.user_dev = user_dev
