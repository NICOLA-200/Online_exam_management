from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
# Create your views here.
from teacher import models as TMODEL
from student import models as SMODEL
from teacher import forms as TFORM
from student import forms as SFORM




def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'exam/index.html')

def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def afterlogin_view(request):
    if is_student(request.user):      
        return redirect('student/student-dashboard')
                
    elif is_teacher(request.user):
        return redirect('teacher/teacher-dashboard')


# def afterlogin_view(request):
#     if is_student(request.user):      
#         return redirect('student/student-dashboard')
                
#     elif is_teacher(request.user):
#         accountapproval=TMODEL.Teacher.objects.all().filter(user_id=request.user.id,status=True)
#         if accountapproval:
#             return redirect('teacher/teacher-dashboard')
#         else:
#             return render(request,'teacher/teacher_wait_for_approval.html')
#     else:
#         return redirect('admin-dashboard')
