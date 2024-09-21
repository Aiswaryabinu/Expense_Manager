from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required



#def add_expense(request):
    #if request.method == 'POST':
       # form = ExpenseForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('expense_list')  # Redirect to an expense list view after saving
    #else:
        #form = ExpenseForm()
    #return render(request, 'add_expense.html', {'form': form})






from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Expense
from collections import defaultdict
import json

@login_required
def expense_list(request):
    # Filter expenses by the current logged-in user
    expenses = Expense.objects.filter(user=request.user)

    # Initialize a dictionary to store totals for each category
    category_totals = defaultdict(float)

    for expense in expenses:
        category_totals[expense.category] += float(expense.amount)

    # Prepare data for pie chart
    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    # Convert the data to JSON for JavaScript
    categories_json = json.dumps(categories)
    totals_json = json.dumps(totals)

    context = {
        'expenses': expenses,
        'categories': categories_json,
        'totals': totals_json
    }
    return render(request, 'expense_list.html', context)

    


# expenseapp/views.py





# expenseapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ExpenseForm

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Associate the expense with the logged-in user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

