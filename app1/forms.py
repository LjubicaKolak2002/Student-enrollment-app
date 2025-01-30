from .models import Predmeti, Korisnik, Upisi
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class PredmetiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('lecturer').queryset = Korisnik.objects.filter(role='profesor')

    class Meta:
        model = Predmeti
        fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'lecturer']



class AddProfesor(UserCreationForm):
    ROLES = (('profesor', 'profesor'),)
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Korisnik
        fields = ['username', 'first_name', 'last_name' ,'email', 'role']


class AddStudent(UserCreationForm):
    ROLES = (('student', 'student'),)
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Korisnik
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'status']


class ChangeStatusForm(ModelForm):
    class Meta:
        model = Upisi
        fields = ['status']



class UpdateStudForm(ModelForm):
    ROLES = (('student', 'student'),)
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Korisnik
        fields = ['username', 'first_name', 'last_name', 'email', 'status', 'role']



class UpdateProfForm(ModelForm):
    ROLES = (('profesor', 'profesor'),)
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = Korisnik
        fields = ['username', 'first_name', 'last_name', 'email', 'role']

        