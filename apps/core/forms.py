from django.forms import ModelForm
from .models import Solution, Test
import django_filters


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='prueba1')

    class Meta:
        model = Solution
        fields = ['user_dev']

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['test_name','difficulty','description','test_desc']

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['user_dev', 'leng_program','test_choice','description','is_done']

class SolutionUpdateForm(ModelForm):
    class Meta:
        model = Solution
        fields = ['leng_program','test_choice','description','is_done']

