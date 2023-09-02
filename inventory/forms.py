from django import forms

from inventory.models import Inventory


class InventoryForm(forms.ModelForm):
    inventory_img = forms.ImageField(required = True)
    class Meta:
        model = Inventory
        fields= ['name', 'status','quantity', 'inventory_img']

class InventoryUpdateForm(forms.ModelForm):
    inventory_img = forms.ImageField(required = True)
    class Meta:
        model = Inventory
        fields= ['name', 'status','quantity', 'is_available', 'inventory_img']
