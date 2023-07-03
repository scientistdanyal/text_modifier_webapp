from django.http import HttpResponse


def index(request):
        nav = '''
            
            <h1>Home</h1>
    
             <li><a href="removepunc">Remove Punctuation</a></li>
             <li><a href="capitalize">Capitalization</a></li>
             <li><a href="newline_remove">New Line Remover</a></li>
             <li><a href="spaceremove">Space Remover</a></li>
             <li><a href="charcount">Charecter Counter</a></li>
            '''
        return HttpResponse(nav)

def removepunc(request):
    return HttpResponse('''<h1>about danyal</h1><br>
    <a href="/">back to main page</a>''')

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