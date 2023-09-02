from django.shortcuts import redirect, render
from django.views import View
from maintenance.forms import MaintenanceForm, MaintenanceUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from maintenance.models import maintenance

# Create your views here.

from django.views import View
from django.contrib import messages

from maintenance.models import maintenance


# Create your views here.
class createmaintenance(View):
    def get(self, request):
        print(request.user)
        form = MaintenanceForm()
        return render(request, 'maintenance/create.html', locals())
    def post(self, request):
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.supervised_by = request.user
            instance.save()
            #send mail or message
            messages.success(request, 'maintenance created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'maintenance/create.html', locals())



class maintenancelist(View):
    def get(self, request):
        user = request.user
        item = maintenance.objects.all()
        return render(request, 'maintenance/maintenancelist.html', locals())



class maintenanceDetail(View):
    def get(self, request, pk):
        item=get_object_or_404(maintenance, pk=pk)
        return render(request, 'maintenance/maintenanceDetail.html', locals())


class Updatemaintenance(View):
    def get(self,request,pk):
        item=get_object_or_404(maintenance, pk=pk)
        form=MaintenanceUpdateForm(instance=item)
        return render(request, 'maintenance/Updatemaintenance.html',locals())
    def post(self,request,pk):
        form=MaintenanceUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            item=get_object_or_404(maintenance, pk=pk)
            item.item = form.cleaned_data['item']
            item.part_repaired =form.cleaned_data['part_repaired']
            item.supervised_by =form.cleaned_data['supervised_by']
            item.location = form.cleaned_data['location']
            item.mechanic_Name = form.cleaned_data['mechanic_Name']
            item.mechanic_Number = form.cleaned_data['mechanic_Number']
            item.is_completed = form.cleaned_data['is_completed']

            item.amount_spent = form.cleaned_data['amount_spent']
            item.description = form.cleaned_data['description']
            
            
            item.save()
            # send email
            messages.success(request,'item update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('list-maintenance')


class Deletemaintenance(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(maintenance, pk=pk)
        # item.delete()
        return render(request, 'maintenance/maintenanceDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(maintenance, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-maintenance')
        