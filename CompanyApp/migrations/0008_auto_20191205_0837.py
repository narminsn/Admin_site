# Generated by Django 2.2.6 on 2019-12-05 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0007_transactionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2019, 12, 5), null=True),
        ),
    ]
