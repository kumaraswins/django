# Generated by Django 2.2.9 on 2020-10-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('last_name', models.CharField(default='', max_length=256)),
                ('email', models.EmailField(default='', max_length=64, unique=True)),
                ('phone', models.CharField(default='', max_length=64, unique=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Regular', 'Regular')], default='admin', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
            ],
        ),
    ]