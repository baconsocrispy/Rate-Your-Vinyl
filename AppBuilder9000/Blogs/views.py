from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blogs_home.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# this function should be ran when the request is receieved and its not
# i think this is the case because the path doesnt have a direction
def new_post(request):
    return request(request, 'post_new.html')

