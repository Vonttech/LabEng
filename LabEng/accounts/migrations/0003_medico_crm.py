# Generated by Django 3.0.4 on 2020-04-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_medico_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='crm',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
