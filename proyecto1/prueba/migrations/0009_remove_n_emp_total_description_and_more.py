# Generated by Django 4.1.7 on 2023-04-09 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0008_rename_nombre_n_empleados_p_n_emp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='n_emp_total',
            name='description',
        ),
        migrations.RemoveField(
            model_name='n_emp_total',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='n_emp_total',
            name='name',
        ),
        migrations.AddField(
            model_name='n_emp_total',
            name='Empleados_Totales',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]