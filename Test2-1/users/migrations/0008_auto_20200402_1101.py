# Generated by Django 3.0.4 on 2020-04-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200402_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('1', 'easy'), ('2', 'general'), ('3', 'difficult')], max_length=10, null=True, verbose_name='等级'),
        ),
    ]
