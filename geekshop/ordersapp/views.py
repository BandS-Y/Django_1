from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from baskets.models import Basket
from mainapp.mixin import BaseClassContextMixin
from ordersapp.forms import OrderForm, OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView, BaseClassContextMixin):
    model = Order
    title = 'MyShop | Список заказов'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)


class OrderCreate(CreateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'MyShop | Создание заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_item = Basket.objects.filter(user=self.request.user)
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=basket_item.count())
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                # basket_item.delete()
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderCreate, self).form_valid(form)


class OrderUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'MyShop | Обновление заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderUpdate, self).form_valid(form)


class OrderDelete(DeleteView, BaseClassContextMixin):
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'MyShop | Удаление заказа'


class OrderDetail(DetailView, BaseClassContextMixin):
    model = Order
    title = 'MyShop | Просмотр заказа'


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))
