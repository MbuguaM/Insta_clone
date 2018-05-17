from django.shortcuts import render

# Create your views here.


def home(request):
    """ displays the landing page """
    return render(request,'all_templates/landing.html')