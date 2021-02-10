# Generated by Django 3.0.1 on 2020-03-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddEmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('designations', models.CharField(default=False, max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('contactno', models.IntegerField(unique=True)),
            ],
        ),
    ]
