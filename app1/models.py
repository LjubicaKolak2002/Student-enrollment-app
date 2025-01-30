from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Korisnik(AbstractUser):
    email = models.EmailField()
    ROLES = (('profesor', 'profesor'), ('student', 'student'))
    role = models.CharField(max_length=50, choices=ROLES)
    STATUS = (('none', 'None'), ('izvanredni student', 'izvanredni student'), ('redovni student', 'redovni student'))
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return ' %s %s' % (self.first_name, self.last_name)



class Predmeti(models.Model):
    IZBORNI = (('DA', 'da'), ('NE', 'ne'))
    name = models.CharField(max_length=255)
    kod = models.CharField(max_length=16)
    program = models.TextField()
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    lecturer = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank=True, null=True) 

    
    def __str__(self):
        return ' %s %s %s %s %s %s %s %s' % (self.name, self.kod, self.program, self.ects, self.sem_red, self.sem_izv, self.izborni, self.lecturer)


class Upisi(models.Model):
    student = models.ForeignKey(Korisnik, on_delete=models.CASCADE, blank=True, null=True, related_name='korisnik')
    predmet = models.ForeignKey(Predmeti, on_delete=models.CASCADE, blank=True, null=True, related_name ='predmeti')
    STATUS = (('upisan', 'Upisan'), ('polozen', 'Polozen'))
    status = models.CharField(max_length=64, choices=STATUS, default='upisan')