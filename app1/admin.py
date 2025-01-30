from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik, Predmeti, Upisi

# Register your models here.

class AdminPredmeti(admin.ModelAdmin):
    fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'lecturer']

admin.site.register(Predmeti, AdminPredmeti)


@admin.register(Korisnik)
class KorisnikAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )


class AdminUpisi(admin.ModelAdmin):
    fields = ['student', 'predmet', 'status']

admin.site.register(Upisi, AdminUpisi)