# Generated by Django 3.2 on 2022-06-26 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=5)),
                ('cycle', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('post_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('post_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.school')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('post_name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.parent')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.school')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.CharField(max_length=10)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_present', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.student')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.school'),
        ),
    ]