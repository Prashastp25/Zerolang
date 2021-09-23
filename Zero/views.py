from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import mimetypes
def index(request):
    return render(request,'index.html')

def create(request):
    return render(request, 'create.html')
def contact(request):
    return render(request,'contact.html')
def main(request):
    return render(request,'final.html',template_con)


