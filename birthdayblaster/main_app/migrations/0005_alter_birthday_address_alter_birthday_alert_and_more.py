# Generated by Django 4.2.5 on 2023-09-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_birthday_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='alert',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='delivery_method',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='relationship',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
