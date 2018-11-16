from django.shortcuts import render

def post_list (request):
    return render(request, 'blog/post_list.html', {})

def about_me (request):
    return render(request, 'blog/about_me.html', {})
    