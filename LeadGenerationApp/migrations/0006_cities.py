# Generated by Django 4.1.3 on 2022-12-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0005_states'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateid', models.IntegerField()),
                ('cityid', models.IntegerField()),
                ('cityname', models.CharField(default='', max_length=45)),
            ],
        ),
    ]
