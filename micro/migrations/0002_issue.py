# Generated by Django 2.1.7 on 2019-03-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('issue', models.CharField(blank=True, max_length=253, null=True)),
            ],
        ),
    ]
