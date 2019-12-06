from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

# from django.contrib.admin.templates
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/company/', views.comp_add_view, name='add'),
    path('edit/company/<int:id>/', views.comp_edit_view, name='edit_comp'),
    path('comp/delete/<int:id>', views.comp_delete, name='comp_delete'),
    path('company/', views.company_list, name='comp_list'),
    path('add/customer/', views.customer_add_view, name='add_customer'),
    path('edit/customer/<int:id>/', views.customer_edit_view, name='edit_cus'),
    path('customer/delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('customer/', views.customer_list, name='customer_list'),
    path('add/person/', views.add_person, name='add_person'),
    path('edit/person/<int:id>/', views.edit_person, name='edit_person'),
    path('person/delete/<int:id>', views.person_delete, name='person_delete'),

    path('persons/', views.person_list, name='person_list'),
    path('add/project/', views.add_project, name='add_project'),
    path('edit/project/<int:id>/', views.edit_project, name='edit_project'),
    path('project/delete/<int:id>', views.project_delete, name='pro_delete'),
    path('projects/', views.project_list, name='project_list'),
    path('add/account/', views.add_account, name='add_account'),
    path('edit/account/<int:id>/', views.edit_account, name='edit_account'),
    path('account/delete<int:id>/', views.account_delete, name='delete_account'),
    path('accounts/', views.account_list, name='account_list'),
    path('add/assignment/', views.add_assignment, name='add_assign'),
    path('edit/assignment/<int:id>/', views.edit_assignment, name='edit_assign'),
    path('assignment/', views.assign_list, name='assign_list'),
    path('assign/delete<int:id>/', views.assign_delete, name='delete_assign'),

    path('add/transaction/', views.add_transaction, name='add_transaction'),
    path('edit/transaction/<int:id>/', views.edit_transaction, name='edit_transaction'),
    path('transaction/delete<int:id>/', views.transaction_delete, name='delete_transaction'),

    path('transactions/', views.transaction_list, name='transaction_list'),

]
