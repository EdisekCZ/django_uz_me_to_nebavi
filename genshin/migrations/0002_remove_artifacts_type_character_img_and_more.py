# Generated by Django 4.0.4 on 2022-04-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genshin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifacts',
            name='type',
        ),
        migrations.AddField(
            model_name='character',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Characters/img', verbose_name='Character Image'),
        ),
        migrations.AlterField(
            model_name='artifacts',
            name='name',
            field=models.CharField(help_text='Enter Artifact Name', max_length=50, unique=True, verbose_name='Artifacts'),
        ),
    ]