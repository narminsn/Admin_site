# Generated by Django 2.2.6 on 2019-12-05 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyApp', '0010_delete_transactionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Expense', 'expense'), ('Revenue', 'revenue'), ('Debt', 'debt')], max_length=10)),
                ('date', models.DateField(default=datetime.date(2019, 12, 5))),
                ('currency', models.CharField(choices=[('AZN', 'AZN'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=4)),
                ('value', models.FloatField()),
                ('azn_value', models.FloatField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='CompanyApp.AccountsModel')),
                ('assignment', models.ForeignKey(limit_choices_to={'parent': False}, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='CompanyApp.AssignmentModel')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompanyApp.CompanyModel')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='CompanyApp.CustomerModel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='CompanyApp.PersonsModel')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompanyApp.ProjectsModel')),
            ],
        ),
    ]