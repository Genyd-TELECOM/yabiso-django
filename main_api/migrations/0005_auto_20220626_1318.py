# Generated by Django 3.2 on 2022-06-26 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0004_alter_parent_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_api.school'),
        ),
        migrations.AddField(
            model_name='registration',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_api.school'),
        ),
    ]
