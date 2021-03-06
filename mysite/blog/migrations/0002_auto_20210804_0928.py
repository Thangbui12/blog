# Generated by Django 3.2.6 on 2021-08-04 09:28

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
