from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())

    password = forms.CharField(widget=forms.PasswordInput())


class AddCompany(forms.ModelForm):
    class Meta:
        model = models.CompanyModel
        fields = ['company_name']




class AddCustomer(forms.ModelForm):
    class Meta:
        model = models.CustomerModel
        fields = ['customer_name']



class AddPerson(forms.ModelForm):
    class Meta:
        model = models.PersonsModel
        fields = ['first_name', 'last_name', 'customer', 'phone', 'email']


class AddProject(forms.ModelForm):
    class Meta:
        model = models.ProjectsModel
        fields = ['name', 'customer', 'person', 'date']


class AddAccount(forms.ModelForm):
    class Meta:
        model = models.AccountsModel
        fields = ['name', 'company', 'type', 'currency']


class AddAssignment(forms.ModelForm):
    class Meta:
        model = models.AssignmentModel
        fields = ['name', 'assignment']


class AddTransaction(forms.ModelForm):
    class Meta:
        model = models.TransactionModel
        fields = ['type', 'date', 'company', 'customer', 'person','project', 'assignment', 'account', 'currency', 'value']