# Generated by Django 4.0 on 2021-12-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poem_name', models.CharField(max_length=128)),
                ('poem', models.CharField(max_length=8192)),
            ],
        ),
    ]
