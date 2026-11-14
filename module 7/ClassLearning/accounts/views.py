from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentCreationForm
from .models import Student


# Create your views here.
def accounts_view(request):
    
    if request.method == "POST":
        print("POST request")
        data = request.POST
        student_form = StudentCreationForm(data)
        if student_form.is_valid():
            student_form.save()
            return redirect('product/')
    else:
        print("GET request")
        student_form = StudentCreationForm()
        
        
        
    context = {
        'student_form' : student_form
    }
    return render(
        request,
        "accounts.html",
        context
    )
    
def update(request, id):
    student = get_object_or_404(Student, id = id)
    if request.method == "POST":
        data = request.POST
        student_form =  StudentCreationForm(data, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect("product")
        
    else:
        student_form = StudentCreationForm(instance=student)
    return render(
            request,
            "update.html",
            context={
                'student_form' : student_form
            },
        )