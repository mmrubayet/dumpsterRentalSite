# Generated by Django 3.2.5 on 2021-07-08 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('abbvr', models.CharField(max_length=2, unique=True)),
                ('article', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('city_detail', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='state.state')),
            ],
        ),
    ]
