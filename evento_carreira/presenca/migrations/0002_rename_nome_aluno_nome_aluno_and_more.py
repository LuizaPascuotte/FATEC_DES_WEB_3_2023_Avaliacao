# Generated by Django 4.2.2 on 2023-06-12 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presenca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='nome',
            new_name='nome_aluno',
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='professor',
            new_name='nome_professor',
        ),
    ]
