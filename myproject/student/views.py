#from django.http import HttpResponse 
# Create your views here.

#def home (request):
 #   return HttpResponse("welcome to D jango")

from django.shortcuts import  get_object_or_404, render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    data = {
        'name':'Devanshi',
        'course':'Django',
        'college':'JG University'
    }

    subject=['python-django','agile','angular','bigdata']
    # students = Student.objects.all()
    return render(request,'index.html',{'data': data,'subject_list':subject, 'marks':80})    
    # return render(request, 'index.html',data)

def contact(request):
    return render(request,'contact.html')   

def about(request):
    return render(request,'about.html') 

def list(request):
    student = Student.objects.all()
    return render(request,'student_crud/list.html',{'students':student})   

# def add(request): 
#     if request.method == "POST":
#         Student.objects.create(
#             name=request.POST['name'],
#                         email=request.POST['email'],
#             mobile=request.POST['mobile'],
#             city=request.POST['city'],
#         )
#         return redirect('list')
#     return render(request,'student_crud/add.html')
def add(request):
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list') 
    else:
      form = StudentForm()

    return render (request,'student_crud/add.html',{'form':form})

# def edit(request, id): 
#     student = get_object_or_404(Student,id=id)
#     if request.method == "POST":
#             student.name = request.POST['name']
#             student.email = request.POST['email']
#             student.mobile = request.POST['mobile']
#             student.city = request.POST['city']
#             student.save()
#             return redirect('list')
#     return render(request, 'student_crud/edit.html',{
#          'student':student
# })

def edit(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        form = StudentForm(request.post,instance=student)
        if form.is_valid():
            form.save()
            return redirect('list') 
        else:
                  form = StudentForm()
            
        return render (request,'student_crud/edit.html',{'form':form})
            

def delete(request, id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect('list')
