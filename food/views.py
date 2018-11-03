from django.shortcuts import render
# get model text from database
from .models import Post

# homepage


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # pases info into our template
    return render(request, 'food/home.html', context)

# create a about page when user wants goes from home. each file is its own object and class so all other http tabs proceding home page will be found in this file


def about(request):
    return render(request, 'food/about.html')
