from django.urls import path

# Use lazy import inside urlpatterns
urlpatterns = [
    path('transactions/', lambda: __import__('transactions.views').views.TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:transaction_id>/', lambda: __import__('transactions.views').views.TransactionDetailUpdate.as_view(), name='transaction-detail-update'),
]

