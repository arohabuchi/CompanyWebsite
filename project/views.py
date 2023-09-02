from django.shortcuts import redirect, render
from django.views import View
from project.forms import projectForm, projectUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from project.models import project

# Create your views here.

from django.views import View
from django.contrib import messages

from project.models import project


# Create your views here.
class createproject(View):
    def get(self, request):
        print(request.user)
        form = projectForm()
        return render(request, 'project/create.html', locals())
    def post(self, request):
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.supervised_by = request.user
            instance.save()
            #send mail or message
            messages.success(request, 'project created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'project/create.html', locals())



class projectlist(View):
    def get(self, request):
        user = request.user
        item = project.objects.all()
        return render(request, 'project/projectlist.html', locals())



class projectDetail(View):
    def get(self, request, pk):
        item=get_object_or_404(project, pk=pk)
        return render(request, 'project/projectDetail.html', locals())


class Updateproject(View):
    def get(self,request,pk):
        item=get_object_or_404(project, pk=pk)
        form=projectUpdateForm(instance=item)
        return render(request, 'project/Updateproject.html',locals())
    def post(self,request,pk):
        form=projectUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            item=get_object_or_404(project, pk=pk)
            item.project_image = form.cleaned_data['project_image']
            item.location = form.cleaned_data['location']
            item.description = form.cleaned_data['description']
            
            item.save()
            # send email
            messages.success(request,'item update successfully')
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('list-project')


class Deleteproject(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(project, pk=pk)
        # item.delete()
        return render(request, 'project/projectDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(project, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-project')
        