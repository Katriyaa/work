# Generated by Django 4.1.4 on 2023-01-18 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
    ]
