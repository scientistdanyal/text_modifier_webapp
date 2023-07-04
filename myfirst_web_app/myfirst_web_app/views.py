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
   extraspacesremover = request.GET.get('extraspacesremover','off')
   charcount = request.GET.get('charcount','off')

   # removal of punctuation
   if removepunc == 'on':
    punctutaions ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctutaions:
            analyzed = analyzed + char
    prams = {"purpose":"Remove Punctuation","analyzed":analyzed}       
    return render(request,'analyze.html',prams)
   
   # capitalization of text
   elif fullcaps == 'on':
    analyzed = djtext.upper()
    prams = {"purpose":"Convert to Uppercase","analyzed":analyzed}
    return render(request,'analyze.html',prams)
   
   # new line remover
   elif newlineremover == 'on':
    analyzed = ""
    for char in djtext:
       if char != '\n':
          analyzed = analyzed + char
    
    prams = {"purpose":"New Lines are Removed","analyzed":analyzed}
    return render(request,'analyze.html',prams)
   
   # extra spaces remover
   elif extraspacesremover == 'on':
    analyzed = ""
    for index,char in enumerate(djtext):
       if djtext[index] ==' ' and djtext == ' ':
          pass
       analyzed = analyzed + char
    
    prams = {"purpose":"Extra Spaces are Removed","analyzed":analyzed}
    return render(request,'analyze.html',prams)
   

   # character count
   elif charcount == 'on':
      analyzed = 0
      analyzed = len(djtext)
      prams = {'purpose':'Count Character','analyzed':analyzed}   
      return render(request,'analyze.html',prams)
   else:
      return HttpResponse('error')

