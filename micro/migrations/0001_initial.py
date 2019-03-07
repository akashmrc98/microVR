# Generated by Django 2.1.7 on 2019-02-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Filters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(blank=True, max_length=150, null=True)),
                ('genere', models.CharField(blank=True, max_length=150, null=True)),
                ('words', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=150)),
                ('label', models.CharField(max_length=150)),
                ('vtype', models.CharField(blank=True, max_length=150, null=True)),
                ('contents', models.CharField(blank=True, max_length=255, null=True)),
                ('genere', models.CharField(blank=True, max_length=150, null=True)),
                ('no_words', models.CharField(blank=True, max_length=1000, null=True)),
                ('no_sentences', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('videos', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Zuke_Subscribed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Zuke_User',
            fields=[
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('dob', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=15)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='zuke_subscribed',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro.Zuke_User'),
        ),
        migrations.AddField(
            model_name='zuke_subscribed',
            name='video_title',
            field=models.ManyToManyField(to='micro.Videos'),
        ),
        migrations.AddField(
            model_name='user_filters',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro.Zuke_User'),
        ),
    ]