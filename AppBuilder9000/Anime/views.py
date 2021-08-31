from django.shortcuts import render
from .models import Description


def anime_home(request):
    descriptions = Description.objects.all()
    return render(request, 'Anime/Anime_index.html', {'descriptions': descriptions})

# #def Anime_create(request):
# #    form = DescriptionForm(data=request.POST or None)
# #    if request.method == "POST" and form.is_valid():
# #        result = form.save()
#         return redirect('Description_get', pk=result.id)
#     else:
#         return render(request, 'Description/create.html', {'form': form})