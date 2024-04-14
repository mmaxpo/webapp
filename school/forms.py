from django import forms
from django.forms import ModelForm, SelectDateWidget
from school.models import Enrollment, Student, Course


class RegisterStudentForm(forms.ModelForm):
    date_of_enrollment = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_of_enrollment', 'grade']


class StudentSearchForm(forms.Form):
    query = forms.CharField(label='search for student',help_text='enter student name')
