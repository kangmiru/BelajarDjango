from django.db import models

# Create your models here.
class Siswa(models.Model):
    GENDER_CHOICE = [
        ('L', 'laki-laki'),
        ('P', 'perempuan')
    ]
    nama = models.CharField(max_length=500)
    alamat = models.CharField(max_length=500)
    tanggal_lahir = models.DateField()
    kelas = models.CharField(max_length=100)
    gender =models.CharField(max_length=1, choices=GENDER_CHOICE)

class Guru(models.Model):
    GENDER_CHOICE = [
        ('L', 'laki-laki'),
        ('P', 'perempuan')
    ]

    nama = models.CharField(max_length=500)
    alamat = models.CharField(max_length=500)
    tanggal_lahir = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    mata_pelajaran = models.CharField(max_length=100)
    honorer = models.BooleanField(default=False)
    pengalaman_mengajar = models.IntegerField()