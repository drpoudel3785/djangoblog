# Generated by Django 4.0.6 on 2022-09-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empcode', models.CharField(default='', max_length=10)),
                ('firstName', models.CharField(max_length=150, null=True)),
                ('middleName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phoneNo', models.CharField(default='', max_length=12, null=True)),
                ('address', models.CharField(default='', max_length=500, null=True)),
                ('exprience', models.CharField(default='', max_length=50, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='', max_length=10, null=True)),
                ('qualification', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
    ]
