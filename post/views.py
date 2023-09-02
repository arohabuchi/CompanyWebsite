from django.shortcuts import render

# Create your views here.
def notfound(requet, exception):
    return render(requet, 'notfound.html')