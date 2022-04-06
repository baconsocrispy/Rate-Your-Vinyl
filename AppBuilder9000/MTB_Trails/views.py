from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def mtb_trails_home(request):
    return render(request, "MTB_Trails/mtb_trails_home.html")
