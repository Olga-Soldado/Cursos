# Generated by Django 3.2.2 on 2021-06-30 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='description',
            field=models.TextField(),
        ),
    ]
