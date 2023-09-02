from django.shortcuts import redirect, render
from django.views import View
from job.forms import jobForm, jobUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from job.models import job

# Create your views here.

from django.views import View
from django.contrib import messages

from job.models import job


# Create your views here.
class createjob(View):
    def get(self, request):
        print(request.user)
        form = jobForm()
        return render(request, 'job/create.html', locals())
    def post(self, request):
        form = jobForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.supervised_by = request.user
            instance.save()
            #send mail or message
            messages.success(request, 'job created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'job/create.html', locals())



class joblist(View):
    def get(self, request):
        user = request.user
        item = job.objects.all()
        return render(request, 'job/joblist.html', locals())



class jobDetail(View):
    def get(self, request, pk):
        item=get_object_or_404(job, pk=pk)
        return render(request, 'job/jobDetail.html', locals())


class Updatejob(View):
    def get(self,request,pk):
        item=get_object_or_404(job, pk=pk)
        form=jobUpdateForm(instance=item)
        return render(request, 'job/Updatejob.html',locals())
    def post(self,request,pk):
        form=jobUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            item=get_object_or_404(job, pk=pk)
            item.client_name = form.cleaned_data['client_name']
            item.location = form.cleaned_data['location']
            item.description = form.cleaned_data['description']
            item.supervised_by = form.cleaned_data['supervised_by']
            item.crew = form.cleaned_data['crew']
            item.expected_Days_of_completion = form.cleaned_data['expected_Days_of_completion']
            item.actual_Days_of_completion = form.cleaned_data['actual_Days_of_completion']
            item.survey_lithology = form.cleaned_data['survey_lithology']
            item.drilling_plan = form.cleaned_data['drilling_plan']
            item.casing_plan = form.cleaned_data['casing_plan']
            item.start_date = form.cleaned_data['start_date']
            item.casing_plan = form.cleaned_data['casing_plan']
            
            item.save()
            # send email
            messages.success(request,'item update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('list-job')


class Deletejob(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(job, pk=pk)
        # item.delete()
        return render(request, 'job/jobDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(job, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-job')
        