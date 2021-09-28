from django.urls import path
from . import views


#story1: step5: create urls.py for your app and homepage
    # urls.py specifies which view is called for a given URL pattern.
    # prior to this is 4. templates
    # urls.py maps URLs to the  apps' views.
    # mapping is done through pairs of: Regular expression or a view in a Django app.

# from django.conf.urls import include                # this address maximum recursion depth exceeded, when base.html includes header.html, and your header.html extends base.html, causing an infinite loop. -->
from django.contrib import admin
from django.urls import path
from . import views  # this use the views.py from it's mainapp


# request sent to switchboard, and it comes to here, then url will say what to do.
# UrlPatterns list = [ 'pattern to watch for', the function to call, "shortcut name"]
# [ 'commands it's looking for', involk the response, or what should show on user's screen]

urlpatterns = [
    path('admin/', admin.site.urls),    # regular expressions, type in xxx.x.x.x:xxxx/admin/ & will see admin.site.urls
    path('', views.RevitFunctions_home, name='RevitFunctions_home'),  # add URL for the html page, views.xxxx will call the function in views.py.
    # only views.home should not have any location. rest should enter what follows http://127.0.0.1:8000/xxxx/
    path('RevitFunctions_futureNav1/', views.RevitFunctions_futureNav1, name='RevitFunctions_futureNav1'),
    path('RevitFunctions_futureNav2/', views.RevitFunctions_futureNav2, name='RevitFunctions_futureNav2'),
    path('RevitFunctions_futureNav3/', views.RevitFunctions_futureNav3, name='RevitFunctions_futureNav3'),
]

