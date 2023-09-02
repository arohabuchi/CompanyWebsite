from django.shortcuts import redirect, render
from django.views import View
from contactForm.forms import contactFormForm, contactFormUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from contactForm.models import contactForm

# Create your views here.

from django.views import View
from django.contrib import messages

from contactForm.models import contactForm


# Create your views here.
class createcontactForm(View):
    def get(self, request):
        print(request.user)
        form = contactFormForm()
        return render(request, 'contactForm/create.html', locals())
    def post(self, request):
        form = contactFormForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.supervised_by = request.user
            instance.save()
            #send mail or message
            messages.success(request, 'contactForm created successfully')
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'contactForm/create.html', locals())



class contactFormlist(View):
    def get(self, request):
        user = request.user
        item = contactForm.objects.all()
        return render(request, 'contactForm/contactFormlist.html', locals())



class DeletecontactForm(View):
    def get(self,request,pk):
        # if request.user is admin or a staff
        item=get_object_or_404(contactForm, pk=pk)
        # item.delete()
        return render(request, 'contactForm/contactFormDelete.html', locals())

    def post(self,request,pk):
        item=get_object_or_404(contactForm, pk=pk)
        if request.method=='POST':
            item.delete()
            messages.success(request,'item update successfully')
        return redirect('list-contactForm')
        