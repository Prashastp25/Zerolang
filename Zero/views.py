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
    print(request.GET)
    arr_desire_wrds = []
    arr_keywords = []
    arr_keywords.append(request.GET.getlist('form'))
    arr_desire_wrds.append(request.GET.getlist('out-word'))
    project_name = request.GET['project-name']
    print(arr_keywords,arr_desire_wrds)
    temp_store = []
    template_con = {}
    file = open("static/main.py","w")
    file_static = open("static/main.py","w")
    file_main = open("main.py","w")
    str = """arr_keywords = %s
arr_desire_wrds = %s
temp_store = []
def main():
    keywords = input()
    desire_wrds = input()
    arr_desire_wrds.append(desire_wrds)
    arr_keywords.append(keywords)
    fin = input()
    temp_store.append(fin)
    for index in range(0, len(arr_keywords)):
        temp_store.append(temp_store[-1].replace(arr_desire_wrds[index],arr_keywords[index]))
    exec(temp_store[-1])

while True:
    main()""" % (arr_keywords[0],arr_desire_wrds[0])
    file.write(str)
    file_static.write(str)
    
    file_main.write(str)
    file.close()
    file_static.close()
    file_main.close()
    num_keywords = []
    for i in range(0,len(arr_desire_wrds[0])):
        num_keywords.append(i) 
    template_con['project_name'] = project_name
    template_con['keywords'] = zip(num_keywords,arr_keywords[0],arr_desire_wrds[0])
    return render(request,'final.html',template_con)


