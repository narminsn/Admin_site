from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from . import forms
from . import models
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from datetime import datetime
# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')

class loginView(LoginView):
    pass



def comp_add_view(request):
    context = {
        'name' : 'Company',
        'form' : forms.AddCompany

    }
    if request.method == 'POST':
        form = forms.AddCompany(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comp_list')
    return render(request, 'add-project.html',context)


def comp_edit_view(request,id):
    data = models.CompanyModel.objects.filter(id=id).last()
    context = {
        'name' : 'Company',
        'form' : forms.AddCompany(instance=data)

    }
    if request.method == 'POST':
        form = forms.AddCompany(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('comp_list')

    return render(request, 'add-project.html',context)

def comp_delete(request, id):
    context = {}

    data = models.CompanyModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('comp_list')

        return render(request, 'include/compdelete.html',context)


def company_list(request):
    context = {
        'name': 'Company',
        'num' : 6
    }
    data = models.CompanyModel.objects.all()
    pagination = Paginator(models.CompanyModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'list-datatable.html',context)


def customer_add_view(request):
    context = {
        'name' : 'Customer',
        'form' : forms.AddCustomer

    }
    if request.method == 'POST':

        form = forms.AddCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comp_list')

    return render(request, 'add-project.html',context)


def customer_edit_view(request,id):
    data = models.CustomerModel.objects.filter(id=id).last()
    context = {
        'name' : 'Customer',
        'form' : forms.AddCustomer(instance=data)

    }
    if request.method == 'POST':

        form = forms.AddCustomer(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_list')

    return render(request, 'add-project.html',context)


def customer_delete(request, id):
    context = {}

    data = models.CustomerModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('customer_list')

        return render(request, 'include/customerdelete.html',context)


def customer_list(request):
    context = {
        'name' : 'Customer',
        'num': 6

    }
    data = models.CustomerModel.objects.all()
    pagination = Paginator(models.CustomerModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'customerlist.html',context)

def add_person(request):
    context = {
        'name': 'Person',
        'form': forms.AddPerson

    }
    if request.method == 'POST':

        form = forms.AddPerson(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    return render(request, 'add-project.html', context)

def edit_person(request,id):
    data = models.PersonsModel.objects.filter(id=id).last()
    context = {
        'name': 'Person',
        'form': forms.AddPerson(instance=data)

    }
    if request.method == 'POST':

        form = forms.AddPerson(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    return render(request, 'add-project.html', context)


def person_delete(request, id):
    context = {}

    data = models.PersonsModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('person_list')

        return render(request, 'include/persondelete.html',context)


def person_list(request):
    context = {
        'name': 'Person',
        'num': 6

    }
    pagination = Paginator(models.PersonsModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'personlist.html',context)


def add_project(request):
    datee = str(datetime.today().date())
    date_list = datee.split('-')
    str_date = f'{date_list[1]}/{date_list[2]}/{date_list[0]}'
    context = {
        'name': 'Project',
        'form': forms.AddProject,
        'datee': str_date

    }

    if request.method == 'POST':
        if request.is_ajax():
            id = request.POST.get('id')
            customers = models.PersonsModel.objects.filter(customer_id=id)
            result = []
            for i in customers:
                obj={
                    'id' : i.id,
                    'name' : i.full_name
                }
                result.append(obj)

            return JsonResponse({
                'data': result
            })

        form = forms.AddProject(request.POST)
        if form.is_valid():
            project = form.save()
            date = request.POST.get('date')
            # datetime_object = datetime.strptime(date, '%m/%d/%y').date()
            print('DATEEE')
            print(date)
            date_pro = date.split('/')
            print(date_pro)
            str_date = f'{date_pro[2]}-{date_pro[0]}-{date_pro[1]}'
            print(type(date))
            project.date = str_date
            project.save()
            return redirect('project_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)


def edit_project(request,id):
    data = models.ProjectsModel.objects.filter(id=id).last()
    datee = str(data.date)
    date_list = datee.split('-')
    str_date = f'{date_list[1]}/{date_list[2]}/{date_list[0]}'

    context = {
        'name': 'Project',
        'form': forms.AddProject(instance=data),
        'datee' : str_date,

    }
    if request.method == 'POST':
        if request.is_ajax():
            id = request.POST.get('id')
            customers = models.PersonsModel.objects.filter(customer_id=id)
            result = []
            for i in customers:
                obj={
                    'id' : i.id,
                    'name' : i.full_name
                }
                result.append(obj)

            return JsonResponse({
                'data': result
            })

        form = forms.AddProject(request.POST,instance=data)
        if form.is_valid():
            project = form.save()
            date = request.POST.get('date')
            # datetime_object = datetime.strptime(date, '%m/%d/%y').date()
            print('DATEEE')
            print(date)
            date_pro = date.split('/')
            print(date_pro)
            str_date = f'{date_pro[2]}-{date_pro[0]}-{date_pro[1]}'
            print(type(date))
            project.date = str_date
            project.save()
            return redirect('project_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)


def project_list(request):
    context = {
        'name': 'Project',
        'num': 6

    }
    pagination = Paginator(models.ProjectsModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    if request.method == 'POST' and request.is_ajax():
        arr = request.POST.getlist('ids')
        print('IDDDDD')
        print(arr)
        for i in arr:
            models.ProjectsModel.objects.filter(id=int(i)).last().delete()
        return JsonResponse({
            'status' : 'ok'
        })

    return render(request, 'projectlist.html',context)


def project_delete(request, id):
    context = {}
    print('WERTHGBDSFGHGFD')
    print(id)
    data = models.ProjectsModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('project_list')

        return render(request, 'include/projectdelete.html',context)


def add_account(request):
    context = {
        'name': 'Account',
        'form': forms.AddAccount

    }
    if request.method == 'POST':

        form = forms.AddAccount(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)

def edit_account(request,id):
    data = models.AccountsModel.objects.filter(id=id).last()
    context = {
        'name': 'Account',
        'form': forms.AddAccount(instance=data)

    }
    if request.method == 'POST':

        form = forms.AddAccount(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)

def account_delete(request, id):
    context = {}
    print('WERTHGBDSFGHGFD')
    print(id)
    data = models.AccountsModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('project_list')

        return render(request, 'include/accountdelete.html',context)


def account_list(request):
    context = {
        'name': 'Account',
        'num': 6

    }
    pagination = Paginator(models.AccountsModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'accountlist.html',context)


def add_assignment(request):
    context = {
        'name': 'Assignment',
        'form': forms.AddAssignment

    }
    if request.method == 'POST':

        form = forms.AddAssignment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)


def edit_assignment(request,id):
    data = models.AssignmentModel.objects.filter(id=id).last()
    context = {
        'name': 'Assignment',
        'form': forms.AddAssignment(instance=data)

    }
    if request.method == 'POST':

        form = forms.AddAssignment(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('assign_list')
        else:
            context['form'] = form
    return render(request, 'add-project.html', context)


def assign_delete(request, id):
    context = {}
    print('WERTHGBDSFGHGFD')
    print(id)
    data = models.AssignmentModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('project_list')

        return render(request, 'include/assigndelete.html',context)


def assign_list(request):
    context = {
        'name' : 'Assignment',
        'num': 6

    }
    pagination = Paginator(models.AssignmentModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'assignlist.html',context)



def add_transaction(request):
    context = {
        'name': 'Transaction',
        'form': forms.AddTransaction

    }
    if request.method == 'POST':
        if request.is_ajax():
            type = request.POST.get('type')
            if type == 'project':
                id = request.POST.get('id_cus')
                id_per = request.POST.get('id_person')
                customers = models.ProjectsModel.objects.filter(customer_id=id, person_id=id_per)
                result = []
                for i in customers:
                    obj = {
                        'id': i.id,
                        'name': i.name
                    }
                    result.append(obj)

                return JsonResponse({
                    'data': result
                })
            else:


                id = request.POST.get('id')
                customers = models.PersonsModel.objects.filter(customer_id=id)
                result = []
                for i in customers:
                    obj={
                        'id' : i.id,
                        'name' : i.full_name
                    }
                    result.append(obj)

                return JsonResponse({
                    'data': result
                })

        form = forms.AddTransaction(request.POST)
        if form.is_valid():
            project = form.save()
            date = request.POST.get('date')
            # datetime_object = datetime.strptime(date, '%m/%d/%y').date()
            date_pro = date.split('/')
            str_date = f'{date_pro[2]}-{date_pro[0]}-{date_pro[1]}'
            project.date = str_date
            project.save()
            return redirect('transaction_list')
        else:
            print('ELSEE')
            context['form'] = form
    return render(request, 'add-project.html', context)


def edit_transaction(request,id):
    data = models.TransactionModel.objects.filter(id=id).last()
    context = {
        'name': 'Transaction',
        'form': forms.AddTransaction(instance=data)

    }
    if request.method == 'POST':
        if request.is_ajax():
            type = request.POST.get('type')
            if type == 'project':
                id = request.POST.get('id_cus')
                id_per = request.POST.get('id_person')
                customers = models.ProjectsModel.objects.filter(customer_id=id, person_id=id_per)
                result = []
                for i in customers:
                    obj = {
                        'id': i.id,
                        'name': i.name
                    }
                    result.append(obj)

                return JsonResponse({
                    'data': result
                })
            else:


                id = request.POST.get('id')
                customers = models.PersonsModel.objects.filter(customer_id=id)
                result = []
                for i in customers:
                    obj={
                        'id' : i.id,
                        'name' : i.full_name
                    }
                    result.append(obj)

                return JsonResponse({
                    'data': result
                })

        form = forms.AddTransaction(request.POST,instance=data)
        if form.is_valid():
            project = form.save()
            date = request.POST.get('date')
            # datetime_object = datetime.strptime(date, '%m/%d/%y').date()
            date_pro = date.split('/')
            str_date = f'{date_pro[2]}-{date_pro[0]}-{date_pro[1]}'
            project.date = str_date
            project.save()
            return redirect('transaction_list')
        else:
            print('ELSEE')
            context['form'] = form
    return render(request, 'add-project.html', context)



def transaction_delete(request, id):
    context = {}
    print('WERTHGBDSFGHGFD')
    print(id)
    data = models.TransactionModel.objects.filter(id=id).last()
    if data:
        context['project'] = data
        if request.method == 'DELETE':
            print('SDFGHJKDERTYHJNBVFDTYHJNB')
            data.delete()
            return redirect('project_list')

        return render(request, 'include/transactiondelete.html',context)



def transaction_list(request):
    context = {
        'name': 'Transaction',
        'num': 6

    }
    pagination = Paginator(models.TransactionModel.objects.all().order_by('-id'), 6)
    context["company"] = pagination.get_page(request.GET.get('page', 1))
    context["page_range"] = pagination.page_range

    return render(request, 'transactionlist.html',context)


