from django.shortcuts import render

from first_app.forms import TestForm



# Create your views here.



def home(request):

    forms=TestForm()



    return render(request,'home.html',{'forms':forms})