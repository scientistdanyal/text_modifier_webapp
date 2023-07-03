from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>Hello world </h1><br> <a href='https://www.google.com/'>Click me</a>''')

def about(request):
    return HttpResponse("about danyal")