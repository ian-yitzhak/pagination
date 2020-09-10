from django.shortcuts import render

from . models import Blog


from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger


from .forms import EmailPostForm





def post_list(request):

    posts = Blog.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')

    try:

        posts = paginator.page(page)

    except PageNotAnInteger:

        posts = paginator.page(1)

    except EmptyPage:

        posts = paginator.page(paginator.num_pages)


    return render(request , 'pagination/index.html' , { 'page': page, 'posts': posts })







