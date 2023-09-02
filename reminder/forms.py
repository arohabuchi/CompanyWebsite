from django import forms
from .models import reminder


class DateInput(forms.DateInput):
    input_type = 'date'

class reminderForm(forms.ModelForm):
    mail = forms.EmailField()
    date_of_action = forms.DateField(widget=DateInput)
    

    class Meta:
        model = reminder
        fields = ['title', 'description', 'is_mail','date_of_action','mail']


class reminderUpdateForm(forms.ModelForm):
    mail = forms.EmailField()

    class Meta:
        model = reminder
        fields = ['title', 'description', 'is_mail','date_of_action','mail']

