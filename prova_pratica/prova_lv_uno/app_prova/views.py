from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("homepage")  
    
def chi_siamo(request):
    return HttpResponse("chi siamo?")

def contatti(args):
    return HttpResponse("contattaci?")
    