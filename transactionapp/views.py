from django.shortcuts import render
from django.views.generic import ListView
from transactionapp.models import Operation

# Create your views here.

def operation_list(request):
    name = request.GET.get('operation_name')
    value = request.GET.get('value')
    operation_list =Operation.objects.filter()
    if name:
        operation_list = operation_list.filter(name__icontains=name)
    if value:
        operation_list = operation_list.filter(value__gte=value)

    context = {
        'operation_list':operation_list
    }
    return render(request,'transactionapp/operation_list.html',context)

class OperationList(ListView):
    model= Operation
