# Generated by Django 3.1 on 2020-11-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('about', models.CharField(max_length=1000)),
                ('symptoms', models.CharField(max_length=1000)),
                ('treatment', models.CharField(max_length=1000)),
            ],
        ),
    ]
