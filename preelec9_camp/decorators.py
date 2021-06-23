from django.contrib.auth.models import User
from django.shortcuts import redirect
def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/camp/')
        return wrapper_function
    return decorator

def registered_only(view_func):
    def wrapper_function(request, *args, **kwargs):
            try:
                if request.user.groups.all()[0].name == '64_student':
                    db = request.user.campdata_64
                elif request.user.groups.all()[0].name == '63_student':
                    db = request.user.campdata_63
                    if db.confirmed == False: return redirect('/camp/')
                return view_func(request, *args, **kwargs) 
            except:
                return redirect('/camp/')
    return wrapper_function