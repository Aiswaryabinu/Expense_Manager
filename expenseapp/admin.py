
from django.contrib import admin
from .models import Expense, FoodExpense, GroceryStationaryExpense, BillsExpense, OtherExpense

admin.site.register(Expense)
admin.site.register(FoodExpense)
admin.site.register(GroceryStationaryExpense)
admin.site.register(BillsExpense)
admin.site.register(OtherExpense)


# Register your models here.
