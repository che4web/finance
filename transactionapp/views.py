from django.shortcuts import render
from django.views.generic import ListView
from transactionapp.models import Operation
from transactionapp.forms import SearchForm,OperationForm

# Create your views here.

def operation_list(request):
    form = SearchForm(request.GET)
    operation_list =Operation.objects.filter()
    if form.is_valid():
        name = form.cleaned_data['operation_name']
        value = form.cleaned_data['value']

        if name:
            operation_list = operation_list.filter(name__icontains=name)
        if value:
            operation_list = operation_list.filter(value__gte=value)

    context = {
        'operation_list':operation_list,
        'form':form
    }
    return render(request,'transactionapp/operation_list.html',context)


def operation_create(request):
    if request.method=='POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OperationForm()


    context = {
        'form':form
    }
    return render(request,'transactionapp/operation_form.html',context)

class OperationList(ListView):
    model= Operation
