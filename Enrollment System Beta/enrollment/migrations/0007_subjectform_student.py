# Generated by Django 3.1.7 on 2021-05-10 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0006_remove_subjectform_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectform',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enrollment.user'),
            preserve_default=False,
        ),
    ]
