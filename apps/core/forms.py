from django.forms import ModelForm
from .models import Solution, Test

# Create the form class.
class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['test_name','difficulty','description','prueba']

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['user_dev', 'lenguaje','description']