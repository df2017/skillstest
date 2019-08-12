from django.forms import ModelForm
from .models import Solution

# Create the form class.
class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['user_dev', 'lenguaje','description']