# Generated by Django 4.1.7 on 2023-04-02 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_login_register_delete_curso_delete_entregable_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='contraseña',
            new_name='contrasena',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
