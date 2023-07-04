from django.http import HttpResponse
from django.shortcuts import render   #for templates

def index(request):
    # program ={'name':'Danyal','place':'Islamabad'}
    return render(request, 'index.html')




def analyse(request):
   #get the text
   djtext = request.GET.get('text','default')
   removepunc = request.GET.get('removepunc','off')
   fullcaps = request.GET.get('fullcaps','off')
   newlineremover = request.GET.get('removeNewLine','off')

   # removal of punctuation
   if removepunc == 'on':
    punctutaions ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    anaylzed = ""
    for char in djtext:
        if char not in punctutaions:
            anaylzed = anaylzed + char
    prams = {"purpose":"Remove Punctuation","anlyzed":anaylzed}       
    return render(request, 'removepunc.html',prams)
   
   # capitalization of text
   elif fullcaps == 'on':
    anaylzed = djtext.upper()
    prams = {"purpose":"Convert to Uppercase","anlyzed":anaylzed}
    return render(request, 'removepunc.html',prams)
   
   # new line remover
   elif newlineremover == 'on':
    anaylzed = ""
    for char in djtext:
       if char != '\n':
          anaylzed = anaylzed + char
    
    prams = {"purpose":"New Lines are Removed","anlyzed":anaylzed}
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