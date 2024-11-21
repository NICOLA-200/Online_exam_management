from django.urls import path
from student import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
]