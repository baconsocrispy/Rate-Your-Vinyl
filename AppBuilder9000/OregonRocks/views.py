from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from .models import RockLoc
from.forms import RockForm
from django.shortcuts import redirect

from geopy.geocoders import Nominatim

def Oregon_Rocks_Home(request):
    return render(request, 'OregonRocks/OregonRocksHome.html')

def Rocks_Create(request):
    form = RockLoc(request)
    if form == 'POST':
        form.save()
    else:
        form = RockLoc()
    context = {
        'form': form,
    }
    return render(request, 'OregonRocks/Rocks_Create.html', context)

def Rock_Locations(request):
    locations = get_object_or_404(RockLoc, pk=pk)
    return render(request, 'OregonRocks/Rock_Locations.html', {'locations': locations})

def Rock_Details(request, pk):
    details = get_object_or_404(RockLoc, pk=pk)
    context = {'details': details}
    return render(request, "OregonRocks/Rock_Details.html", context)
#geolocator = Nominatim(user_agent="location")


# class ListCreateGenericViews(generics.ListCreateAPIView):
#     queryset = get_object_or_404(RockLoc)
#     serializer_class = RockLoc
#
#     def perform_create(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)
#
#
# class RockUpdateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_object_or_404(RockLoc)
#     serializer_class = RockLoc
#
#     def perform_update(self, serializer):
#         address = serializer.initial_data["address"]
#         g = geolocator.geocode(address)
#         lat = g.latitude
#         lng = g.longitude
#         pnt = Point(lng, lat)
#         print(pnt)
#         serializer.save(location=pnt)