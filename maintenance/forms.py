from django import forms

from maintenance.models import maintenance


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = maintenance
        fields= ['item', 'part_repaired', 'location', 'mechanic_Name','mechanic_Number', 'amount_spent','description','is_completed']

class MaintenanceUpdateForm(forms.ModelForm):
    class Meta:
        model = maintenance
        fields= ['item', 'part_repaired','supervised_by', 'location', 'mechanic_Name','mechanic_Number', 'amount_spent','description','is_completed']
