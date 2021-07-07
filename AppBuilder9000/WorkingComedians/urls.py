from django.urls import path, include
from WorkingComedians import views

urlpatterns = [
    path('', views.workingcomedians_home, name='home'),
]

#maybe the path is wrong?

#from 'WorkingComedians'(name of my app/folder) import
#views(view.py). now it seems the 'views' file

#the function 'home' is called and should render the
#url 'WorkingComedians(inside the template folder(django recognizes
# the directory because of the __init__ file))/WorkingComedians_home.html file

#the home.html file should display the base.html file because line 1 'extends'
#the base file.