from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from transactionapp.models import Operation
from transactionapp.forms import SearchForm,OperationForm

from rest_framework import routers, serializers, viewsets
from rest_framework.filters import OrderingFilter

# Create your views here.

import django_filters
from django_filters import rest_framework as filters

class OperationFilter(django_filters.FilterSet):
    search = filters.CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Operation
        fields = '__all__'


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    filter_backends = (OrderingFilter,filters.DjangoFilterBackend,)
    ordering_fields = '__all__'
    filterset_class = OperationFilter

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
def operation_list_json(request):
    form = SearchForm(request.GET)
    operation_list =Operation.objects.filter()
    if form.is_valid():
        name = form.cleaned_data['operation_name']
        value = form.cleaned_data['value']

        if name:
            operation_list = operation_list.filter(name__icontains=name)
        if value:
            operation_list = operation_list.filter(value__gte=value)
    operation_list_json = []
    for x in operation_list:
        operation_list_json.append({
            'id':x.id,
            'name':x.name,
            'value':x.value,
        })

    return JsonResponse(operation_list_json,safe=False)



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
