from django.http import HttpResponse
from django.shortcuts import render   #for templates

def index(request):
    # program ={'name':'Danyal','place':'Islamabad'}
    return render(request, 'index.html')




def analyse(request):
   #get the text
   djtext = request.GET.get('text','default')
   removepunc = request.GET.get('removepunc','off')
#    print(removepunc)
#    print(djtext)
   punctutaions ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   anaylzed = ""
   for char in djtext:
       if char not in punctutaions:
           anaylzed = anaylzed + char

   prams = {"purpose":"Remove Punction","anlyzed":anaylzed}       
   return render(request, 'removepunc.html',prams)

# def capitalize(request):
#     return HttpResponse('''<h1>about danyal</h1><br>
#     <a href="/">back to main page</a>''')

# def newline_remove(request):
#     return HttpResponse('''<h1>about danyal</h1><br>
#     <a href="/">back to main page</a>''')

# def spaceremove(request):
#     return HttpResponse('''<h1>about danyal</h1><br>
#     <a href="/">back to main page</a>''')
# def charcount(request):
#     return HttpResponse('''<h1>about danyal</h1><br>
#     <a href="/">Back to main page</a>''')