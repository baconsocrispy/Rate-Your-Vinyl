from django.shortcuts import render

def VillagerRegistry_Index(request):
    return render(request, 'Villager_Registry/villager_home.html')

