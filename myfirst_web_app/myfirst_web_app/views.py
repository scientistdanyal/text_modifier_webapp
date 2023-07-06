from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('removeNewLine', 'off')
    extraspacesremover = request.POST.get('extraspacesremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == 'on' or newlineremover == 'on' or charcount == 'on' or extraspacesremover == 'on' :
        if removepunc == 'on':
            punctuations = '''!()-[]};{:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed += char
            prams = {"purpose": "Remove Punctuation", "analyzed": analyzed}
        djtext = analyzed    
            

        if fullcaps == 'on':
            analyzed = djtext.upper()
            prams = {"purpose": "Convert to Uppercase", "analyzed": analyzed}
        djtext = analyzed
            

        if newlineremover == 'on':
            analyzed = ""
            for char in djtext:
                if char != '\n':
                    analyzed += char
            prams = {"purpose": "New Lines are Removed", "analyzed": analyzed}
        djtext = analyzed
           

        if extraspacesremover == 'on':
            analyzed = ""
            for index, char in enumerate(djtext):
                if djtext[index] == ' ' and djtext[index - 1] == ' ':
                    pass
                analyzed += char
            prams = {"purpose": "Extra Spaces are Removed", "analyzed": analyzed}
        djtext = analyzed
            


        if charcount == 'on':
            analyzed = len(djtext)
            prams = {"purpose": "Count Characters", "analyzed": analyzed}
        djtext = analyzed
            

        return render(request, 'analyze.html', prams)
    else:
        return HttpResponse('error')
