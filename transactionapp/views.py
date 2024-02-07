from django.shortcuts import render
from django.views.generic import ListView
from transactionapp.models import Operation

# Create your views here.

def operation_list(request):
    context = {
        'operation_list':Operation.objects.all()
    }
    return render(request,'transactionapp/operation_list.html',context)

class OperationList(ListView):
    model= Operation
