from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
    path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
    path('teachersignup', views.teacher_signup_view,name='teachersignup'),
    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacherclick', views.teacherclick_view),
    path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
    path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),


path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),

path('see-question/<int:pk>', views.see_question_view,name='see-question'),

 path('charts/', views.charts_view, name='charts_view'),
]