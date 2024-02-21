from django import forms
from transactionapp.models import Operation


class SearchForm(forms.Form):
    operation_name = forms.CharField(label="Название", max_length=100)
    value = forms.IntegerField(label="сумма")

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields= "__all__"
