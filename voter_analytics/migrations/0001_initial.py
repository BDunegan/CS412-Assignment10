# Generated by Django 5.1.2 on 2024-11-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('street_num', models.IntegerField()),
                ('street_name', models.TextField()),
                ('appartment_num', models.IntegerField()),
                ('zip', models.IntegerField()),
                ('dob', models.DateField()),
                ('dor', models.DateField()),
                ('affiliation', models.TextField()),
                ('precinct', models.IntegerField()),
                ('v20state', models.BooleanField()),
                ('v21town', models.BooleanField()),
                ('v21primary', models.BooleanField()),
                ('v22general', models.BooleanField()),
                ('v23town', models.BooleanField()),
                ('voter_score', models.IntegerField()),
            ],
        ),
    ]