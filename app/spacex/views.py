from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Wrong username or password')

    return render(request, 'spacex/sign.html')


def logout_user(request):
    logout(request)
    return redirect('main')


def main(request):
    # q = request.GET.get('q') if request.GET.get('q') != None else ''
    # searched = Item.objects.filter(Q(name__icontains=q) & Q(description__contains=q))
    categories = Category.objects.all()
    form = SingUp
    context = {
        'form': form,
        'cat': categories
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


def register(request):
    context = {

    }
    return render(request, 'spacex/sign.html', context)


def add_new(request):
    context = {

    }
    return render(request, 'spacex/add_new.html', context)


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
                username = cd['username'],
                email = cd['email'],
                message = cd['message']
            )
            try:
                pc.save()
                messages.success(request, 'Message was sent!')
            except:
                messages.error(request, 'Message was sent!')

    return render(request, 'spacex/contact.html', context)