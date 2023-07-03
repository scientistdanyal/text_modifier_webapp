from django.http import HttpResponse
from django.shortcuts import render   #for templates

def index(request):
    program ={'name':'Danyal','place':'Islamabad'}
    return render(request, 'index.html',program)




def removepunc(request):
   return render(request, 'page1.html')

def capitalize(request):
    return HttpResponse('''<h1>about danyal</h1><br>
    <a href="/">back to main page</a>''')

def newline_remove(request):
    return HttpResponse('''<h1>about danyal</h1><br>
    <a href="/">back to main page</a>''')

def spaceremove(request):
    return HttpResponse('''<h1>about danyal</h1><br>
    <a href="/">back to main page</a>''')
def charcount(request):
    return HttpResponse('''<h1>about danyal</h1><br>
    <a href="/">Back to main page</a>''')