# Generated by Django 4.2.5 on 2023-09-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('telefone', models.BigIntegerField(verbose_name='telefone')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
            ],
        ),
    ]
