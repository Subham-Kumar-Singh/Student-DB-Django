from django.forms import ModelForm
from .models import Student


class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'