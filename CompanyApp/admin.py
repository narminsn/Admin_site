from django.contrib import admin
from django.utils.html import format_html
# from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from . import models
#
#
# # Register your models here.

class Accountinline(admin.StackedInline):
    model = models.AccountsModel
    extra = 1

class Personsline(admin.StackedInline):
    model = models.PersonsModel
    extra = 1


#
@admin.register(models.CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/companymodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/companymodel/{}/delete/">Delete</a>', obj.id)

    # inlines = [Accountinline]
    list_display = ['company_name', 'azn_value', 'ACTIONS','ACTION' ]
    exclude = ['value']
    list_per_page = 5




@admin.register(models.CustomerModel)
class CompanyAdmin(admin.ModelAdmin):




    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/customermodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/customermodel/{}/delete/">Delete</a>', obj.id)

    inlines = [Personsline]
    list_display = ['customer_name', 'projects_num', 'azn_value', 'ACTIONS','ACTION']
    list_per_page = 5



@admin.register(models.AccountsModel)
class CompanyAdmin(admin.ModelAdmin):
    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/accountsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/accountsmodel/{}/delete/">Delete</a>', obj.id)

    list_display = ['name', 'company', 'currency', 'value', 'azn_value', 'ACTIONS','ACTION' ]
    list_per_page = 5
    exclude = ['azn_val']


@admin.register(models.PersonsModel)
class CompanyAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/personsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/personsmodel/{}/delete/">Delete</a>', obj.id)

    exclude = ['full_name']
    list_display = ['full_name', 'customer','projects_num','azn_value',  'ACTIONS','ACTION' ]
    list_per_page = 5



@admin.register(models.ProjectsModel)
class ProjectAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/delete/">Delete</a>', obj.id)

    list_display = ['name', 'customer',  'person', 'date','ACTIONS','ACTION']
    widget = ['make_published']
    exclude = ['ex_person', 'ex_customer']
    list_per_page = 5







#
@admin.register(models.TransactionModel)
class TransactionAdmin(admin.ModelAdmin):
    # def get_export_formats(self):
    #
    #     formats = (
    #         base_formats.CSV,
    #
    #     )
    #     return [f for f in formats if f().can_export()]
    #
    # def get_import_formats(self):
    #
    #     formats = (
    #         base_formats.CSV,
    #
    #     )
    #     return [f for f in formats if f().can_export()]

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/transactionmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/transactionmodel/{}/delete/">Delete</a>', obj.id)

    def Value(self, obj):
        color = 'red'
        if obj.type == 'Expense' :
            color = 'red'
            return format_html('<b style="color:{};"> {}</b>',
            color,obj.value
            )
        else:
            color = 'green'
            return format_html('<b style="color:{};">+ {}</b>',
                               color, obj.value
                               )

    Value.admin_order_field = 'closed'

    list_display = ['date', 'company', 'customer','person', 'assignment' , 'account',  'Value', 'currency', 'ACTIONS', 'ACTION']
    list_filter = ['date', 'customer', 'customer','person','account']
    ordering = ('date',)
    list_per_page = 5
    exclude = ['azn_value']

# admin.site.register(models.TransactionModel)

@admin.register(models.AssignmentModel)
class AssignmentAdmin(admin.ModelAdmin):

    def ACTIONS(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/change/">EDIT</a>', obj.id)

    def ACTION(self,obj):
        return format_html('<a class="btn" href="/admin/CompanyApp/projectsmodel/{}/delete/">Delete</a>', obj.id)


    list_display = ['name','azn_value',  'ACTIONS', 'ACTION']
    exclude = ['parent']
