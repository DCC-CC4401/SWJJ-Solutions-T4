# Generated by Django 2.1.3 on 2019-05-16 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCurso', models.CharField(help_text='Nombre del curso ', max_length=250)),
                ('codigoCurso', models.CharField(help_text='Codigo curso ', max_length=8)),
                ('numSeccionCurso', models.IntegerField(help_text='Numero seccion del curso')),
                ('anioCurso', models.IntegerField(help_text='Año del curso ')),
                ('semesterCurso', models.IntegerField(help_text='Semestre ')),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Puntaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('texto', models.CharField(max_length=200)),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Criterio')),
            ],
        ),
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion_minima', models.TimeField(verbose_name='Duración Mínima')),
                ('duracion_maxima', models.TimeField(verbose_name='Duración Máxima')),
                ('dataTable', models.FilePathField(path='./RubricasDataTables')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('app_paterno', models.CharField(blank=True, max_length=50, null=True)),
                ('app_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('isAdmin', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='criterio',
            name='rubrica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Rubrica'),
        ),
    ]
