from django.shortcuts import render, redirect
from .forms import *
from .decoraters import unauthenticated_user, allowed_users, admins_only
from django.contrib.auth.decorators import login_required
from .decoraters import *
from .models import *
# Create your views here.


@login_required
@allowed_users(allowed_roles=['vendor head', 'super-admin', 'admin'])
def home(request):
    userroles = request.user.profile.roles.values_list('rolename', flat=True)
    userpermissions = []
    for r in userroles:
        myrole = role.objects.get(rolename=r)
        rolepermissions = myrole.permissions.values_list(
            'permissiontype', flat=True)
        for p in rolepermissions:
            if p not in userpermissions:
                userpermissions.append(p)
    staff = User.objects.filter(profile__head__username=request.user.username)
    context = {'userroles': userroles,
               'userpermissions': userpermissions, 'staff': staff}
    return render(request, 'users/home.html', context)


@login_required
@allowed_users(allowed_roles=['vendor head', 'super-admin', 'admin'])
def add_staff(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newuser = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password1')
            )
            newuser._role = "vendor staff"
            newuser._vendorhead = request.user.username
            newuser.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
@admins_only
def dashboard(request):
    context = {}
    return render(request, 'users/dashboard.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)
