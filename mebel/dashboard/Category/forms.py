from django import forms

from sayt.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
