from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('removeNewLine', 'off')
    extraspacesremover = request.GET.get('extraspacesremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]};{:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        prams = {"purpose": "Remove Punctuation", "analyzed": analyzed}
        return render(request, 'analyze.html', prams)

    elif fullcaps == 'on':
        analyzed = djtext.upper()
        prams = {"purpose": "Convert to Uppercase", "analyzed": analyzed}
        return render(request, 'analyze.html', prams)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed += char
        prams = {"purpose": "New Lines are Removed", "analyzed": analyzed}
        return render(request, 'analyze.html', prams)

    elif extraspacesremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index - 1] == ' ':
                pass
            analyzed += char
        prams = {"purpose": "Extra Spaces are Removed", "analyzed": analyzed}
        return render(request, 'analyze.html', prams)

    elif charcount == 'on':
        analyzed = len(djtext)
        prams = {"purpose": "Count Characters", "analyzed": analyzed}
        return render(request, 'analyze.html', prams)

    else:
        return HttpResponse('error')
