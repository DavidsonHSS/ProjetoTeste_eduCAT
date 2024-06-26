# Generated by Django 5.0.3 on 2024-03-31 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_alter_tarefa_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
