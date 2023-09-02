from django import forms

from project.models import project


class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields= ['project_image', 'location', 'description']

class projectUpdateForm(forms.ModelForm):
    class Meta:
        model = project
        fields= ['project_image', 'location', 'description']
