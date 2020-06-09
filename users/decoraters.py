from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            role = None
            role = request.user.profile.roles.values_list(
                'rolename', flat=True)[0]
            if role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to see this vendor head page Becoz you are staff member")
        return wrapper_func
    return decorator


def admins_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = None
        if request.user.profile.roles.exists():
            role = request.user.profile.roles.all()[0].rolename
        if role.find('admin') != -1:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func
