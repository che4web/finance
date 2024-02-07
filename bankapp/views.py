from django.shortcuts import render
from bankapp.models import BankCard

# Create your views here.
def bankcard_list(request):
    context = {
        'bankcard_list':BankCard.objects.all()
    }
    return render(request,'bankapp/bankcard_list.html',context)

def bankcard_detail(request,pk):
    context = {
        'bankcard':BankCard.objects.get(id=pk)
    }
    return render(request,'bankapp/bankcard_detail.html',context)
