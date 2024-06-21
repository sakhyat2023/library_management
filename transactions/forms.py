from django import forms
from .models import TransactionsModel


class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionsModel
        fields = ["amount", "transactions_type"]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop("account", None)
        super().__init__(*args, **kwargs)
        self.fields["transactions_type"].disable = True
        self.fields["transactions_type"].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "block w-full px-3.5 py-2 text-gray-900 outline-none border border-black"
                }
            )

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_purchase = self.account.balance
        return super().save(commit)

class DepositFrom(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get("amount")
        if amount < min_deposit_amount:
            raise forms.ValidationError(f"You need at least {min_deposit_amount} $")
        return amount
