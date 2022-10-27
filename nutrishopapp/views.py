from django.shortcuts import render
from .models import Blog
from .models import Trending
from .models import Popular
from .models import Newrelease
from .models import Sleep
from .models import Protein







# Create your views here.

def home(request):
    '''render the home page'''
    trending=Trending.objects.all()
    blog=Blog.objects.all()
    return render(request ,'index.html', {'trending':trending, 'blog':blog})

def services(request):
    '''render services page'''
    return render(request, 'services.html')

def about(request):
    '''render about us page'''
    return render(request, 'about.html')

def supplement(request):
    '''render supplement page'''
    popular=Popular.objects.all()
    protein=Protein.objects.all()
    new=Newrelease.objects.all()
    sleep=Sleep.objects.all()

    return render(request, 'supplements.html', {'popular':popular, 'protein':protein , 'new':new, 'sleep':sleep})

def product(request, post_id):
    '''render product page'''
    print(post_id)
    product=Blog.objects.get(id=post_id)
    trending=Trending.objects.all()
    return render(request , 'product-page.html' ,{'trending':trending, 'product':product}  )