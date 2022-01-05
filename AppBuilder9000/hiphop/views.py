from django.shortcuts import render, redirect, get_object_or_404
import requests
import json


def hiphop_home(request):
    # this will return user to hip hop home page
    return render(request, 'hiphop_home.html')

