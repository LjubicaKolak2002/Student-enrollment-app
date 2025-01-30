"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test_view, name='test'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('review_subjects/', views.review_subjects, name='review_subjects'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('update_subject/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('review_subjects_details/<int:subject_id>/', views.review_subjects_details, name='review_subjects_details'),
    path('professors_list/', views.professors_list, name='professors_list'),
    path('students_list/', views.students_list, name='students_list'),
    path('add_professor/', views.add_professor, name='add_professor'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('update_professor/<int:professor_id>/', views.update_professor, name='update_professor'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('students_on_subject/<int:subject_id>/', views.students_on_subject, name='students_on_subject'),
    path('front_page/', views.front_page, name='front_page'),
    path('professor_subjects/<int:professor_id>/', views.professor_subjects, name='professor_subjects'),
    path('students_on_subject_admin/<int:subject_id>/', views.students_on_subject_admin, name='students_on_subject_admin'),
    path('subject_enrollment/<int:student_id>/<int:subject_id>/', views.subject_enrollment, name='subject_enrollment'),
    path('delete_subject/<int:student_id>/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('students_passed_subject/<int:subject_id>/', views.students_passed_subject, name='students_passed_subject'),
    path('change_status/<int:subject_id>/<int:student_id>/', views.change_status, name='change_status'),
    path('enrollment_form_student/<int:student_id>/', views.enrollment_form_student, name='enrollment_form_student'),
    path('enrolled_not_passed/<int:subject_id>/', views.enrolled_not_passed, name='enrolled_not_passed'),
    path('enrollment_form_admin/<int:student_id>/', views.enrollment_form_admin, name='enrollment_form_admin'),
    path('welcome_site/', views.welcome_site, name='welcome_site'),
    path('make_enrollment_form/<int:student_id>/', views.make_enrollment_form, name='make_enrollment_form'),
   

   
]