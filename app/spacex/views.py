from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from .models import *


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Wrong username or password')
    context = {
        'page': page
    }
    return render(request, 'spacex/sign.html', context)


def sign_up(request):

    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        used = User.objects.filter(email=request.POST.get('email'))
        print(used)
        if not used:
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, ' Success! You can login now')
                    logout(request)
                    return redirect('main')
                except:
                    messages.error('Something gone wrong, try later')
        else:
            messages.error(request, ' This email address is already in our database')

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'spacex/sign_up.html', context)


def logout_user(request):
    logout(request)
    return redirect('main')


@login_required(login_url='/login')
def profile(request):
    items = Item.objects.filter(owner=request.user)
    context = {
        'user': request.user,
        'items': items
    }
    return render(request, 'spacex/profile.html', context)


@login_required(login_url='/login')
def edit_profile(request):

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()


    form = UserForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'spacex/edit_profile.html', context)


def vendor(request, id):
    if request.user.id == id:
        return redirect('profile')
    seller = User.objects.get(id=id)
    items = Item.objects.filter(owner=id)
    context = {
        'vendor': seller,
        'items': items
    }
    return render(request, 'spacex/vendor.html', context)


def main(request):
    categories = Category.objects.all()
    random = Item.objects.order_by('?')[0:8]
    form = SingUp
    context = {
        'form': form,
        'cat': categories,
        'random': random
    }
    return render(request, 'spacex/main.html', context)


def category(request, slug):
    items = Item.objects.filter(category__slug=slug)
    count = items.count()
    context = {
        'items': items,
        'amount': count
    }
    return render(request, 'spacex/category.html', context)


def item(request, id):
    item = Item.objects.get(id=id)
    similar = Item.objects.filter(Q(name__icontains=item.name[0:10]))[1:7]
    owner = item.owner
    vendor_items = Item.objects.filter(owner=item.owner)
    count = vendor_items.count()
    context = {
        'item': item,
        'similar': similar,
        'owner': owner,
        'amount': count
    }
    return render(request, 'spacex/item.html', context)



@csrf_exempt
@login_required(login_url='/login')
def add_to_basket(request,id):
    user = request.user
    add = Basket.objects.filter(user=user.id)
    if add:
        pc = Basket.objects.get(user=user.id)
        it = Item.objects.get(id=id)
        pc.items.add(it)
        pc.save()
        return HttpResponse('Added to basket')
    else:
        pc = Basket(
            user = user
        )
        pc.save()
        it = Item.objects.get(id=id)
        pc.items.add(it)
        pc.save()
        return HttpResponse('Added to basket')


@login_required(login_url='/login')
def delete_item(request, id):
    try:
        Item.objects.filter(id=id).delete()
        messages.success(request, 'Item was deleted')
        return redirect('main')
    except:
        messages.error(request, 'Something gone wrong, try later')


def register(request):
    context = {

    }
    return render(request, 'spacex/sign.html', context)


@login_required(login_url='/login')
def add_new(request):
    if request.method == 'POST':
        new_item = AddNewItemForm(request.POST)
        if new_item.is_valid():
            cd = new_item.cleaned_data
            pc = Item(
                name = cd['name'],
                description=cd['description'],
                image=cd['image'],
                price=cd['price'],
                category=cd['category'],
                owner= request.user
            )
            try:
                pc.save()
                messages.success(request, 'Item was just added!')
                return redirect('main')
            except:
                messages.error(request, 'Something gone wrong, try again later')
    form = AddNewItemForm
    context = {
        'form': form
    }
    return render(request, 'spacex/add_new.html', context)


@login_required(login_url='/login')
def update_item(request, id):
    item = Item.objects.get(id=id)
    form = AddNewItemForm(instance=item)
    context = {
        'form': form,
        'id': item.id
    }
    if request.method == 'POST':
        form = AddNewItemForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Item was updated')
                return redirect('main')
            except:
                messages.error()

    return render(request, 'spacex/update.html', context)


def contact(request):
    form = Contact()
    context = {
        'form': form
    }
    if request.method == "POST":
        message = Contact(request.POST)
        if message.is_valid():
            cd = message.cleaned_data
            pc = ContactMessage(
                username=cd['username'],
                email=cd['email'],
                message=cd['message']
            )
            try:
                pc.save()
                messages.success(request, 'Message was sent!')
            except:
                messages.error(request, 'Message was sent!')

    return render(request, 'spacex/contact.html', context)
