# Generated by Django 5.0.3 on 2024-03-31 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]