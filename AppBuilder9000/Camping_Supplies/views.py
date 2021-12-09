from django.shortcuts import get_object_or_404, redirect, render


def Camping_Supplies_Home(request):
    return render(request, 'Camping_Supplies_Home.html'),
