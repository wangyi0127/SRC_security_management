# Generated by Django 4.1.7 on 2023-03-13 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('srcmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leakinformation',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='srcmodel.project'),
            preserve_default=False,
        ),
    ]