# Generated by Django 4.1.4 on 2023-01-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='end',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start',
        ),
        migrations.AddField(
            model_name='education',
            name='desc',
            field=models.TextField(default='eeeeeeeeeeee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='start_end_date',
            field=models.CharField(default='12222222223', max_length=20),
            preserve_default=False,
        ),
    ]
