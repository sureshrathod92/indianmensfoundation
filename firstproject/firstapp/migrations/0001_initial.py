# Generated by Django 4.0.4 on 2022-07-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=60)),
                ('cmob', models.IntegerField()),
                ('cmail', models.EmailField(max_length=254)),
                ('caddr', models.CharField(max_length=50)),
            ],
        ),
    ]
