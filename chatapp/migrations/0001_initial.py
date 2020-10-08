# Generated by Django 3.1.2 on 2020-10-06 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnePlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Illness name')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='description')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='updated date')),
            ],
        ),
        migrations.CreateModel(
            name='UserOnePlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cured_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='cured date')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='add date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('oneplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.oneplace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_month', models.IntegerField(blank=True, default=None, null=True, verbose_name='birth month')),
                ('birth_year', models.IntegerField(blank=True, default=None, null=True, verbose_name='birth year')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
