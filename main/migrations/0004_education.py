# Generated by Django 4.1.4 on 2023-01-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_expertise_language_profile_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=300)),
                ('start', models.CharField(max_length=10)),
                ('end', models.CharField(max_length=10)),
            ],
        ),
    ]
