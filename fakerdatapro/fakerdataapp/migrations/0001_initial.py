# Generated by Django 5.1.1 on 2024-10-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('telugu', models.IntegerField()),
                ('hindi', models.IntegerField()),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('social', models.IntegerField()),
                ('hall_ticket', models.IntegerField()),
            ],
        ),
    ]
