from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PredmetiForm, ChangeStatusForm, UpdateProfForm, UpdateStudForm, AddProfesor, AddStudent
from .models import Korisnik, Predmeti, Upisi
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, student_required, profesor_required

# Create your views here.

def test_view(request):
    return HttpResponse('<h4>Prvi view uspjesno kreiran...</h4>')


def front_page(request):
    return render(request, 'front_page.html')


def welcome_site(request):
    return render(request, 'welcome_site.html')


#pregled predmeta (admin)
@admin_required
@login_required
def review_subjects(request):
    subjects = Predmeti.objects.all()
    return render(request, 'review_subjects.html', {'subjects':subjects})
    

#promjena liste predmeta(admin)
@admin_required
def update_subject(request, subject_id):
    subject_id = Predmeti.objects.get(id = subject_id)

    if request.method == 'GET':
            subject_to_update = PredmetiForm(instance = subject_id)
            return render(request, 'update_subject.html', {'form': subject_to_update})
    
    elif request.method == 'POST':
            subject_to_update = PredmetiForm(request.POST, instance = subject_id)
            if subject_to_update.is_valid():
                subject_to_update.save()
                return redirect('review_subjects')
    else:
        return HttpResponse("Dogodila se greska!")



#pregled predmeta detalji (admin)
@admin_required
def review_subjects_details(request, subject_id):
    subject = Predmeti.objects.filter(id = subject_id)
    return render(request, 'review_subjects_details.html', {'subject':subject[0]})


#dodavanje novog predmeta (admin)
@admin_required
def add_subject(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            subjectForm = PredmetiForm()
            return render(request, 'add_subject.html', {'form': subjectForm})

        elif request.method == 'POST' and request.user.is_authenticated:
            subjectForm = PredmetiForm(request.POST)
            if subjectForm.is_valid():
                subjectForm.save()
                return redirect('review_subjects')            
            else:
                return HttpResponseNotAllowed()


#pregled liste studenata(admin)
@admin_required
def students_list(request):
    students = Korisnik.objects.filter(role = "student")
    return render(request, 'students_list.html', {'students':students})


#pregled liste profesora(admin)
@admin_required
def professors_list(request):
    professors = Korisnik.objects.filter(role = "profesor")
    return render(request, 'professors_list.html', {'professors':professors})



#pregled popisa studenta za svaki pojedinacni predmet(admin)
@admin_required
def students_on_subject_admin(request, subject_id):
    subject_name = Predmeti.objects.get(id = subject_id).name
    subject = Upisi.objects.filter(predmet = subject_id)
    return render(request, 'students_on_subject_admin.html', {'subject':subject, 'subject_name':subject_name})


#dodavanje studenta (admin)
@admin_required
def add_student(request):
     if request.user.is_superuser:
        if request.method == 'GET':
            userForm = AddStudent()
            return render(request, 'add_student.html', {'form': userForm})

        elif request.method == 'POST' and request.user.is_authenticated:
            userForm = AddStudent(request.POST)
            if userForm.is_valid():
                userForm.save()
                return redirect('students_list')            
            else:
                return HttpResponse('Pogreska')


#dodavanje profesora (admin)
@admin_required
def add_professor(request):
     if request.user.is_superuser:
        if request.method == 'GET':
            userForm = AddProfesor()
            return render(request, 'add_professor.html', {'form': userForm})

        elif request.method == 'POST' and request.user.is_authenticated:
            userForm = AddProfesor(request.POST)
            if userForm.is_valid():
                userForm.save()
                return redirect('professors_list')            
            else:
                return HttpResponse('Pogreska')


#editiranje studenta(admin)
@admin_required
def update_student(request, student_id):
    student = Korisnik.objects.get(id = student_id)

    if request.user.is_superuser:
        if request.method == 'GET':
            student_to_update = UpdateStudForm(instance = student)
            return render(request, 'update_student.html', {'form': student_to_update})
    
        elif request.method == 'POST':
            student_to_update = UpdateStudForm(request.POST, instance = student)
            if student_to_update.is_valid():
                student_to_update.save()
                return redirect('students_list')
        else:
            return HttpResponse("Dogodila se greska!")


#editiranje profesora(admin)
@admin_required
def update_professor(request, professor_id):
    professor = Korisnik.objects.get(id = professor_id)

    if request.user.is_superuser:
        if request.method == 'GET':
            professor_to_update = UpdateProfForm(instance = professor)
            return render(request, 'update_professor.html', {'form': professor_to_update})
    
        elif request.method == 'POST':
            #print(request.POST)
            professor_to_update = UpdateProfForm(request.POST, instance = professor)
            if professor_to_update.is_valid():
                professor_to_update.save()
                return redirect('professors_list')
        else:
            return HttpResponse("Dogodila se greska!")
   


#upisni list studenta (admin)
@admin_required
def enrollment_form_admin(request, student_id):
    student = Korisnik.objects.get(id = student_id)
    enroll_form = Upisi.objects.filter(student = student_id)
    enroll_subjects = Predmeti.objects.filter(id__in=enroll_form.values('predmet'))

    return render(request, 'enrollment_form_admin.html', {'enroll_form': enroll_form, 'student': student, 'enroll_subjects':enroll_subjects})



#izrada upisnog lista(admin)
@admin_required
def make_enrollment_form(request, student_id):
    student = Korisnik.objects.get(id = student_id)
    enroll_form = Upisi.objects.filter(student = student_id)
    enroll_subjects = Predmeti.objects.filter(id__in=enroll_form.values('predmet'))
    subject=Predmeti.objects.exclude(id__in=enroll_form.values('predmet_id'))

    return render(request, 'make_enrollment_form.html', {'enroll_form': enroll_form, 'student': student, 'subjects': subject, 'enroll_subjects':enroll_subjects})


#pregled popisa studenta za predmet prijavljenog profesora(profesor)
@profesor_required
def students_on_subject(request, subject_id):
    rows = Upisi.objects.filter(predmet_id = subject_id)
    subject = Predmeti.objects.get(id = subject_id)

    return render(request, 'students_on_subject.html', {'data':rows, 'subject':subject})
    

#pregled liste predmeta prijavljenog profesora(profesor)
@profesor_required
def professor_subjects(request, professor_id):
    subjects = Predmeti.objects.filter(lecturer = professor_id)
    professor = Korisnik.objects.get(id = professor_id)

    return render(request, 'professor_subjects.html', {'data':subjects, 'professor':professor})



#popis studenta koji su polozili predmet(profesor)
@profesor_required
def students_passed_subject(request, subject_id):
    rows = Upisi.objects.filter(predmet = subject_id).filter(status = 'polozen')
    subject = Predmeti.objects.get(id = subject_id).name

    return render(request, 'students_passed_subject.html', {'data':rows, 'subject':subject})


#studenti koji su upisali predmet, ali nisu jos polozili(profesor)
@profesor_required
def enrolled_not_passed(request, subject_id):
    rows = Upisi.objects.filter(predmet = subject_id)
    subject_name = Predmeti.objects.get(id = subject_id).name

    student_arr = []
    for student in rows:
        if (student.status == 'upisan' and student.status != 'polozen'):
            student_arr.append(student.student)
        
    return render(request, 'enrolled_not_passed.html', {'students':student_arr, 'subject_name':subject_name})



#mijenjanje statusa predmeta(profesor/admin)
@profesor_required
def change_status(request, subject_id, student_id):
    subject = Upisi.objects.get(predmet = subject_id, student = student_id)
    subject_name = Predmeti.objects.get(id = subject_id).name
    student_name = Korisnik.objects.filter(id = student_id).values('first_name', 'last_name')

    if request.method == 'GET':
        subject_data = ChangeStatusForm(instance=subject)
        return render(request, 'change_status.html', {'form':subject_data, 'subject':subject_name, 'student':student_name[0]})

    elif request.method == 'POST':
        subject_data = ChangeStatusForm(request.POST, instance=subject)
        if subject_data.is_valid():
            subject_data.save()
            if request.user.is_authenticated and request.user.is_superuser:
                return redirect('enrollment_form_admin', student_id)
            elif request.user.is_authenticated and request.user.role == 'profesor':
                return redirect('students_on_subject', subject_id)


#upis predmeta (student)
@student_required
def subject_enrollment(request, student_id, subject_id):
    student = Korisnik.objects.get(id = student_id)
    subject = Predmeti.objects.get(id = subject_id)

    if request.method == 'GET':
        return render(request, 'subject_enrollment.html', {'subject':subject, 'student':student})
    elif request.method == 'POST':
        upisi = Upisi(status='upisan', predmet_id = subject.id, student_id = student.id)
        upisi.save()
        if request.user.is_superuser:
             return redirect('make_enrollment_form', student_id)
        elif request.user.role == 'student':
            return redirect('enrollment_form_student', student_id) 


#ispis predmeta (student)
@student_required
def delete_subject(request, student_id, subject_id):
    subject = Upisi.objects.filter(predmet = subject_id, student_id = student_id)
    student = Korisnik.objects.get(id = student_id)
    subject_name = Predmeti.objects.get(id = subject_id).name

    if request.method == 'GET':
        return render(request, 'delete_subject.html', {'subject':subject, 'student':student, 'subject_name':subject_name})
    elif request.method == 'POST':
        subject.delete()
        return redirect('enrollment_form_student', student_id)



#upisni list (student)
@student_required
def enrollment_form_student(request, student_id):
    student = Korisnik.objects.get(id = student_id)
    enroll_form = Upisi.objects.filter(student = student_id)
    enroll_subjects = Predmeti.objects.filter(id__in=enroll_form.values('predmet'))
    subject=Predmeti.objects.exclude(id__in=enroll_form.values('predmet_id'))

    return render(request, 'enrollment_form_student.html', {'enroll_form': enroll_form, 'student': student, 'subjects': subject, 'enroll_subjects':enroll_subjects})

