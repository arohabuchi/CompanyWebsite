from django import forms

from job.models import job

class DateInput(forms.DateInput):
    input_type = 'date'
class jobForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
     
    class Meta:
        model = job
        fields= ['client_name', 'location','description', 'supervised_by','crew','expected_Days_of_completion','actual_Days_of_completion','survey_lithology','drilling_plan','casing_plan','start_date']
        widgets= {
            'survey_lithology':forms.FileInput(attrs={'accept':'.pdf'}),
            'drilling_plan':forms.FileInput(attrs={'accept':'.pdf'}),
            'casing_plan':forms.FileInput(attrs={'accept':'.pdf'})
        }

class jobUpdateForm(forms.ModelForm):
    class Meta:
        model = job
        fields= ['client_name', 'location','description', 'supervised_by','crew','expected_Days_of_completion','actual_Days_of_completion','survey_lithology','drilling_plan','casing_plan','start_date']
