from django.shortcuts import render,  redirect, get_object_or_404

# Create your views here.








def Drones_home(request):
    return render(request, 'Drones/Drones_home.html')

