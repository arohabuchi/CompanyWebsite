from django.shortcuts import redirect, render
from django.views import View
from inventory.forms import InventoryForm, InventoryUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from inventory.models import Inventory

# Create your views here.

from django.views import View
from django.contrib import messages


# Create your views here.
class create(View):
    def get(self, request):
        print(request.user)
        form = InventoryForm()
        return render(request, 'inventory/create.html', locals())
    def post(self, request):
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.status=="Bad":
                instance.is_available=False
            instance.user = request.user
            instance.save()
            #send mail or message
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'inventory/create.html', locals())



class inventorylist(View):
    def get(self, request):
        user = request.user
        item = Inventory.objects.all()
        return render(request, 'inventory/inventorylist.html', locals())



class inventoryDetail(View):
    def get(self, request, pk):
        item = Inventory.objects.get(pk=pk)
        return render(request, 'inventory/inventoryDetail.html', locals())


class UpdateInventory(View):
    def get(self,request,pk):
        item = Inventory.objects.get(pk=pk)
        form=InventoryUpdateForm(instance=item)
        return render(request, 'inventory/Updateinventory.html',locals())
    def post(self,request,pk):
        form=InventoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            item = Inventory.objects.get(pk=pk)
            item.name = form.cleaned_data['name']
            item.user = request.user
            item.status = form.cleaned_data['status']
            item.quantity = form.cleaned_data['quantity']
            item.is_available = form.cleaned_data['is_available']
            item.inventory_img = form.cleaned_data['inventory_img']
            item.save()
            # send email
            messages.success(request,'item update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('list-inventory')


class DeleteInventory(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(Inventory, pk=pk)
        # item.delete()
        return render(request, 'inventory/inventoryDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(Inventory, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-inventory')
        