from django import forms

class InstructorLoginForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
