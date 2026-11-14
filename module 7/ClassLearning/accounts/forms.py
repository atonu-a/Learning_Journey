from django import forms
from accounts.models import Student

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'