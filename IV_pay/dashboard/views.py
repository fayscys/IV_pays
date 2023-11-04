from django.views.generic import DetailView, ListView
from .models import UserAccount, MobileTopUp, BillPayment, MoneyTransfer, FrequentPayment

# user account view

class UserAccountDetailView(DetailView):
    model = UserAccount
    template_name = 'user_account_details.html'
    context_object_name = 'user_account'

# mobile top-up view

class MobileTopUpListView(ListView):
    model = MobileTopUp
    template_name = 'mobile_top_up_list.html'
    context_object_name = 'mobile_topups'

# bill payment view

class BillPaymentListView(ListView):
    model = BillPayment
    template_name = 'bill_payment_list.html'
    context_object_name = 'bill_payments'

# money transfer view

class MoneyTransferListView(ListView):
    model = MoneyTransfer
    template_name = 'money_transfer_list.html'
    context_object_name = 'money_transfers'

# frequent payment view

class FrequentPaymentListView(ListView):
    model = FrequentPayment
    template_name = 'frequent_payment_list.html'
    context_object_name = 'frequent_payments'



