from django.shortcuts import render


def homepage(request):
    return render(request, 'ChessOpenings/chess_index.html')




# Create your views here.
