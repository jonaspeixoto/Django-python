# Generated by Django 2.2.6 on 2022-07-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('Sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
            ],
        ),
    ]
