# Generated by Django 4.2.4 on 2023-08-22 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=500)),
                ('alamat', models.CharField(max_length=500)),
                ('tanggal_lahir', models.DateField()),
                ('gender', models.CharField(choices=[('L', 'laki-laki'), ('P', 'perempuan')], max_length=1)),
                ('mata_pelajaran', models.CharField(max_length=100)),
                ('honorer', models.BooleanField(default=False)),
                ('pengalaman_mengajar', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=500)),
                ('alamat', models.CharField(max_length=500)),
                ('tanggal_lahir', models.DateField()),
                ('kelas', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('L', 'laki-laki'), ('P', 'perempuan')], max_length=1)),
            ],
        ),
    ]
