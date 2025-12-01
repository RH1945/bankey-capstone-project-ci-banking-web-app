from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BankeyAccount, Card, Transaction

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BankeyAccount, Card, Transaction


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # show extra fields in admin
    fieldsets = UserAdmin.fieldsets + (
        ("Bankey extra info", {"fields": ("full_name", "dob")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Bankey extra info", {"fields": ("dob",)}),
    )
    list_display = ("username", "email", "full_name", "dob", "is_staff", "is_superuser")
    search_fields = ("username", "email", "full_name")


@admin.register(BankeyAccount)
class BankeyAccountAdmin(admin.ModelAdmin):
    list_display = ("user", "acc_number", "acc_type", "currency", "acc_balance", "created_on")
    list_filter = ("acc_type", "currency", "created_on")
    search_fields = ("acc_number", "user__username", "user__email")


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("account", "card_number", "card_type", "card_balance", "expiration_date", "created_on")
    list_filter = ("card_type", "expiration_date")
    search_fields = ("card_number", "account__acc_number", "account__user__username")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "amount", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("sender__username", "receiver__username")
