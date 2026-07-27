#from django.http import HttpResponse 
# Create your views here.

#def home (request):
 #   return HttpResponse("welcome to D jango")

from django.shortcuts import render

def home(request):
    data = {
        'name':'Devanshi',
        'course':'Django',
        'college':'JG University'
    }

    subject=['python-django','agile','angular','bigdata']
    return render(request,'index.html',{'data': data,'subject_list':subject, 'marks':80})    
    # return render(request, 'index.html',data)

def contact(request):
    return render(request,'contact.html')   

def about(request):
    return render(request,'about.html') 

def list(request):
    return render(request,'student_crud/list.html')   
  
