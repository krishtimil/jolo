from django.shortcuts import render, redirect
from .forms import ShopCreateForm, ServiceCreateForm, ClientRegisterForm, AppointmentRegisterForm # TODO
from django.utils.text import slugify


def shop_create(request):
    if request.method == 'POST':
        form = ShopCreateForm(request.POST)
        if form.is_valid():
            form.save(user_id = request.user.id)
            cd = form.cleaned_data # TODO
            return redirect('dashboard', shop_slug=slugify(cd['shop_name']))
    else:
        form = ShopCreateForm()
        return render(request, 'shop/shop_create.html', {'form': form})

def service_create(request, shop_slug): #TODO: provide shop slug to view form url
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST)
        if form.is_valid():          
            form.save(shop_slug)
            return redirect('service_list')
    else:
        form = ServiceCreateForm()
        return render(request, 'shop/service_create.html', {'form': form, "shop_slug": shop_slug})


# CLIENT
def client_register(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientRegisterForm()
        return render(request, 'client/client_register.html', {'form': form})

def appointment_register(request, shop_slug, service_slug, client_id):
    if request.method == 'POST':
        form = AppointmentRegisterForm(request.POST)
        if form.is_valid():
            form.save() # TODO: client_name, shop_slug, service_slug
            return redirect('appointment_list')
    else:
        form = AppointmentRegisterForm()
        return render(request, 'appointment/appointment_register.html', {'form': form})