from django.shortcuts import render

def home (request):
    return render(request, 'blog/home.html', {})

def about_me (request):
    return render(request, 'blog/about_me.html', {})
    
def proj_list (request):
    return render(request, 'blog/proj_list.html', {})
    