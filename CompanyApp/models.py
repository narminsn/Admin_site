from django.db import models
from datetime import date
# from .request import arr

# def exchange(val,cur):
#     if cur != 'AZN':
#         data = list(filter(lambda x: x['code'] == cur, arr))
#         value = data[0]['value']['$']
#         azn = val * value
#         return round(azn,2)
#     else:
#         return val

class CompanyModel(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

    def azn_value(self):
        arr = self.account.all()
        val = 0
        for i in arr:
            val += i.azn_value()
        return val


class CustomerModel(models.Model):
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_name

    def projects_num(self):
        return len(self.projects.all())

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value
        return val



class PersonsModel(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    full_name = models.CharField(max_length=255, default='')
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,related_name='persons')
    phone = models.CharField(max_length=125)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.full_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_name = f'{self.first_name} {self.last_name}'

        return super(PersonsModel, self).save()

    def projects_num(self):
        return len(self.projects.all())

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value
        return val

class ProjectsModel(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(CustomerModel,on_delete=models.CASCADE, related_name='projects')

    person = models.ForeignKey(PersonsModel,
                               on_delete=models.CASCADE,
                               related_name='projects'
                               )

    date = models.DateField(default=date.today(), null=True, blank=True)

    def __str__(self):
        return self.name




class AccountsModel(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE,related_name='account')
    OFFİCİAL = 'RƏSMİ'
    UNOFFİCİAL = 'QEYRİ-RƏSMİ'

    type_choices = [
        (OFFİCİAL, 'Official'),
        (UNOFFİCİAL, 'Unofficial'),
    ]
    type = models.CharField(
        max_length=25,
        choices=type_choices,

    )
    AZN = "AZN"
    EUR = 'EUR'
    USD = 'USD'

    currency_choices = [
        (AZN, 'Azn'),
        (EUR, 'Eur'),
        (USD, 'Usd')
    ]
    currency = models.CharField(
        max_length=4,
        choices=currency_choices
    )



    def __str__(self):
        return self.name

    def value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val+=i.value
        return val

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value

        return round(val,2)







class AssignmentModel(models.Model):
    name = models.CharField(max_length=255)
    assignment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                   limit_choices_to={'parent': True}
                                   )
    parent = models.BooleanField(default=False)


    def __str__(self):
        return self.name


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.assignment:
            self.parent = True
        return super(AssignmentModel, self).save()

    def azn_value(self):
        arr = self.transactions.all()
        val = 0
        for i in arr:
            val += i.azn_value
        return val





class TransactionModel(models.Model):
    currency_choices = [
        ('Expense', 'expense'),
        ('Revenue', 'revenue'),
        ('Debt', 'debt'),
    ]
    type = models.CharField(max_length=10,choices=currency_choices)
    date = models.DateField(default=date.today())
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='transactions')
    person = models.ForeignKey(PersonsModel, on_delete=models.CASCADE, related_name='transactions')
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentModel, on_delete=models.CASCADE,
                                   related_name='transactions',
                                   limit_choices_to={'parent': False}
                                   )
    account =  models.ForeignKey(AccountsModel, on_delete=models.CASCADE,
                                 related_name='transactions')
    AZN = "AZN"
    EUR = 'EUR'
    USD = 'USD'

    currency_choices = [
        (AZN, 'AZN'),
        (EUR, 'EUR'),
        (USD, 'USD')
    ]
    currency = models.CharField(
        max_length=4,
        choices=currency_choices
    )
    value = models.FloatField()
    azn_value = models.FloatField(default=0)


    # def save(self, force_insert=False, force_update=False, using=None,
        #      update_fields=None):
        #
        #
        #
        # if self.type == 'Expense':
        #     self.value = 0-self.value
        #
        # azn_value = exchange(self.value, self.currency)
        # self.azn_value = azn_value
        # return super(TransactionModel, self).save()


