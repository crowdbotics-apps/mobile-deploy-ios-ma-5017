# Generated by Django 2.2.12 on 2020-06-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id2', models.BigIntegerField()),
                ('id3', models.BigIntegerField()),
            ],
        ),
    ]
