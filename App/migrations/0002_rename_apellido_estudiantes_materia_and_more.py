# Generated by Django 4.1.3 on 2022-12-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiantes',
            old_name='apellido',
            new_name='materia',
        ),
        migrations.RenameField(
            model_name='tutores',
            old_name='apellido',
            new_name='materia',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='materias',
        ),
        migrations.RemoveField(
            model_name='tutores',
            name='correp',
        ),
    ]