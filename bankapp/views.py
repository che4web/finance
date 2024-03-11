from django.shortcuts import render
from bankapp.models import BankCard




from rest_framework import routers, serializers, viewsets

# Create your views here.

import django_filters
from django_filters import rest_framework as filters

class BankCardFilter(django_filters.FilterSet):
    class Meta:
        model = BankCard
        # fields = '__all__'
        exclude ="img"


class BankCardSerializer(serializers.ModelSerializer):
    img_url = serializers.CharField(read_only=True)
    class Meta:
        model = BankCard
        fields = "__all__"

class BankCardViewSet(viewsets.ModelViewSet):
    queryset = BankCard.objects.all()
    serializer_class = BankCardSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BankCardFilter



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
