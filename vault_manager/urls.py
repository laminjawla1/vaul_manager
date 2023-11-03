from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (cashier_deposits, supervisor_deposits, dashboard, reports, my_borrows, bank_deposits,
                    UpdateSupervisorAccount, UpdateCashierAccount,
                    approve_supervisor_deposit, refunds, ledger, accounts, withdrawals,
                    UpdateWithdrawCash, my_withdrawals, UpdateBankDeposit,
                    daily_supervisor_reports, UpdateSupervisorReporting, UpdateCashierReporting, disapprove_supervisor_report,
                    daily_cashier_reports, approve_cashier_report, approve_supervisor_report,
                    UpdateBorrowCash, borrows, currency_transactions, UpdateCurrencyTransact, UpdateReturnCashierAccount,
                    bank_deposits, disapprove_supervisor_deposit)

urlpatterns = [
    path("currency_transactions", currency_transactions, name="currency_transactions"),
    path("currency_transactions/<int:pk>/update/", UpdateCurrencyTransact.as_view(), name="update_currency_transaction"),
    path("agents/refunds/", refunds, name='refunds'),
    path("supervisor/reports/<int:pk>/update", UpdateSupervisorReporting.as_view(), name='update_supervisor_reporting'),
    path("cashier/reports/<int:pk>/update", UpdateCashierReporting.as_view(), name='update_cashier_reporting'),
    path("supervisor/cashier/reports/<int:pk>/update", UpdateReturnCashierAccount.as_view(), name='update_return_cashier_account'),
    path("supervisors/reports/history", daily_supervisor_reports, name='daily_supervisor_reports'),
    path("cashiers/reports/history", daily_cashier_reports, name='daily_cashier_reports'),
    path("agents/logs", ledger, name='ledger'),
    path("accounts", accounts, name='accounts'),
    path("withdrawals", withdrawals, name='withdrawals'),
    path("bank_deposits", bank_deposits, name='bank_deposits'),
    path("bank_deposits", bank_deposits, name='bank_deposits'),
    path("borrows", borrows, name='borrows'),
    path("my_withdrawals", my_withdrawals, name='my_withdrawals'),
    path("my_borrows", my_borrows, name='my_borrows'),
    path("deposits/cashiers", cashier_deposits, name='cashier_deposits'),
    path("deposits/supervisors", supervisor_deposits, name='supervisor_deposits'),
    path("dashboard/", dashboard, name="dashboard"),
    path("me/reports/", reports, name='reports'),
    path("approve_supervisor_report", approve_supervisor_report, name="approve_supervisor_report"),
    path("approve_cashier_report", approve_cashier_report, name="approve_cashier_report"),
    path("disapprove_supervisor_deposit", disapprove_supervisor_deposit, name="disapprove_supervisor_deposit"),
    path("approve_supervisor_deposit", approve_supervisor_deposit, name="approve_supervisor_deposit"),
    path("disapprove_supervisor_report", disapprove_supervisor_report, name="disapprove_supervisor_report"),
    path("supervisor_deposit/<int:pk>/update", UpdateSupervisorAccount.as_view(), name="update_supervisor_deposit"),
    path("cashier_deposit/<int:pk>/update", UpdateCashierAccount.as_view(), name="update_cashier_deposit"),
    path("withdrawals/<int:pk>/update", UpdateWithdrawCash.as_view(), name="update_withdrawal_request"),
    path("bank_deposits/<int:pk>/update", UpdateBankDeposit.as_view(), name="update_bank_deposit_request"),
    path("borrows/<int:pk>/update", UpdateBorrowCash.as_view(), name="update_borrow_request"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)