
from django import forms

class BranchForm(forms.Form):
    degree = forms.CharField(label='degree', max_length=100)
    branch = forms.CharField(label='branch', max_length=100)
    semester = forms.CharField(label='semester', max_length=100)