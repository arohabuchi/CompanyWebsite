import datetime
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from reminder.forms import reminderForm, reminderUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from reminder.models import reminder

# Create your views here.
from django.core.mail import send_mail


from django.views import View
from django.contrib import messages

from reminder.models import reminder
from reminder.task import send_reminder_email


# Create your views here.
class createreminder(View):
    def get(self, request):
        print(datetime.datetime.now().date())
        form = reminderForm()
        return render(request, 'reminder/create.html', locals())
    
    def post(self, request):
        form = reminderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_by = request.user
            # lllllll33333333333333333333333
            send_reminder_email.delay()
            
            remObj = reminder.objects.filter(is_mail=True)
            for obj in remObj:
                if datetime.datetime.now().date() == obj.date_of_action:
                    print("sameeeeeeeeee from task")
                    print("it is today")
                else:
                    print("Not todayyyyy from taskk")
                # ?lllllllllllllllllllllllllllllllllllllllllllllllllllll
                
            instance.save()
            #send mail or message
            messages.success(request, 'reminder created successfully')
        
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'reminder/create.html', locals())



class reminderlist(View):
    def get(self, request):
        user = request.user
        item = reminder.objects.all()
        return render(request, 'reminder/reminderlist.html', locals())



class reminderDetail(View):
    def get(self, request, pk):
        item=get_object_or_404(reminder, pk=pk)
        return render(request, 'reminder/reminderDetail.html', locals())


class Updatereminder(View):
    def get(self,request,pk):
        item=get_object_or_404(reminder, pk=pk)
        form=reminderUpdateForm(instance=item)
        return render(request, 'reminder/Updatereminder.html',locals())
    def post(self,request,pk):
        form=reminderUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            item=get_object_or_404(reminder, pk=pk)
            item.title = form.cleaned_data['title']
            item.description = form.cleaned_data['description']
            item.is_mail = form.cleaned_data['is_mail']
            item.date_of_action = form.cleaned_data['date_of_action']
            item.mail = form.cleaned_data['mail']
            
            item.save()
            # send email
            messages.success(request,'item update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('list-reminder')


class Deletereminder(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(reminder, pk=pk)
        # item.delete()
        return render(request, 'reminder/reminderDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(reminder, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-reminder')

# from .task import test_func

# def test(request):
#     test_func()
#     return HttpResponse("Done")