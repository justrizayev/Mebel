from django import forms

from dashboard.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
