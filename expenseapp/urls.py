from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
    # other paths
]
