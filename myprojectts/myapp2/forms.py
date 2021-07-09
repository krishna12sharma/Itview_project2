from django.forms import ModelForm

from.models import Student
#create Model Form(bades on table you have created)
# class StudentForm(ModelForm):
#     class Meta:  #data about data
#         model=Student
#         fields='__all__'

from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(label="SName",max_length=50)
    marks = forms.CharField(label="SMArks", max_length=50)
    city = forms.CharField(label="SCity", max_length=50)