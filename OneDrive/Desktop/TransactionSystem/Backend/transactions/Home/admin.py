from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # What columns to show in list view
    list_display = (
        'transaction_id',
        'user',
        'amount',
        'beneficiary_name',
        'status',
        'created_at',
    )

    # Clickable field (opens detail page)
    list_display_links = ('transaction_id',)

    # Filters on right side
    list_filter = ('status', 'created_at')

    # Search bar (top right)
    search_fields = (
        'transaction_id',
        'account_number',
        'ifsc_code',
        'beneficiary_name',
        'user__username',
    )

    # Fields editable directly from list view (optional)
    list_editable = ('status',)

    # Read-only fields (important for security)
    readonly_fields = (
        'transaction_id',
        'created_at',
        'updated_at',
    )

    # Group fields nicely in detail view
    fieldsets = (
        ('User Info', {
            'fields': ('user',)
        }),
        ('Transaction Details', {
            'fields': (
                'transaction_id',
                'amount',
                'account_number',
                'ifsc_code',
                'beneficiary_name',
            )
        }),
        ('Status & Admin Action', {
            'fields': ('status', 'admin_remark')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

