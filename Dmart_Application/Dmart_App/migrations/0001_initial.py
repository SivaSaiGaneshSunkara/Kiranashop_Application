# Generated by Django 3.0.8 on 2020-07-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('theater', models.CharField(max_length=30)),
                ('movie', models.CharField(max_length=30)),
                ('chair_seats', models.CharField(max_length=30)),
                ('balcony_seats', models.CharField(max_length=30)),
                ('seat_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('contact', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=12)),
                ('dob', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
