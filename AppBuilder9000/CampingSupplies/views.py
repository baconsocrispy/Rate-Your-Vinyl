from django.shortcuts import get_object_or_404, redirect, render


def Camping_Supplies_Home(request):
    #this function will take the request object and use it to find and display the Camping_Supplies_Home.html

    return render(request, 'Camping_Supplies_Home.html')
