# Generated by Django 3.0.6 on 2020-10-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogTitle',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'posts'},
        ),
    ]
