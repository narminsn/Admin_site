# Generated by Django 2.2.6 on 2019-12-04 17:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('RƏSMİ', 'Official'), ('QEYRİ-RƏSMİ', 'Unofficial')], max_length=25)),
                ('currency', models.CharField(choices=[('AZN', 'Azn'), ('EUR', 'Eur'), ('USD', 'Usd')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(blank=True, limit_choices_to={'parent': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='CompanyApp.AssignmentModel')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('full_name', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='CompanyApp.CustomerModel')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date(2019, 12, 4))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='CompanyApp.CustomerModel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='CompanyApp.PersonsModel')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Expense', 'expense'), ('Revenue', 'revenue'), ('Debt', 'debt')], max_length=10)),
                ('date', models.DateField(default=datetime.date(2019, 12, 4))),
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
        migrations.AddField(
            model_name='accountsmodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='CompanyApp.CompanyModel'),
        ),
    ]