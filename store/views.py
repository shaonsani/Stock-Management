from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView 
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

def store(req):
    query = req.GET.get('search_item')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    context = {'products':products}
    return render(req,'store/store.html',context)

@login_required
def sell(req,pk):
    data = Product.objects.get(pk=pk)
    if req.method =='POST':
        form =SellForm(req.POST)
        if form.is_valid():
            val=form.cleaned_data['quantity']
            ''' Create History object to save the data to it'''
            history = History()
            history.name = data.name
            history.quantity = int(val)
            history.price = data.price
            history.total = int(val)*data.price
            history.save()
            p = Product.objects.get(pk=pk)
            if p.quantity - int(val) >=0:
                p.quantity = p.quantity - int(val)
            else:
                p.quantity = 0
            p.save()
            return HttpResponseRedirect(reverse('APP:store'))
    else:
        form =SellForm()
    return render(req,'store/sell.html',context={'data':data,'form':form})
@login_required
def history(req,data):
    total=0
    if data!=1:
        data = data[0:10]
        total = History.objects.filter(date__icontains=data).aggregate(Sum('total'))
    sell = History.objects.filter(date__icontains=data)
    return render(req,'store/history.html',context={'sell':sell,'total':total})

class ProductAdd(LoginRequiredMixin,CreateView):
    model = Product
    fields = '__all__'
    template_name = 'store/add_product.html'

class ProductUpdate(LoginRequiredMixin,UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'store/update_product.html'

def address(req):
    context = {}
    return render(req,'store/address.html',context)





