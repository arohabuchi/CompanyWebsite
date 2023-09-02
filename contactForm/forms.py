from django import forms

from contactForm.models import contactForm

    
class contactFormForm(forms.ModelForm):    
    class Meta:
        model = contactForm
        fields= ['name', 'email','title', 'description']

class contactFormUpdateForm(forms.ModelForm):
    class Meta:
        model = contactForm
        fields= ['name', 'email','title', 'description']
        
