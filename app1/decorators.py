from django.shortcuts import redirect


def profesor_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.role == 'profesor' or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return redirect('front_page')
    return wrap


def student_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.role == 'student' or request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return redirect('front_page')
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return redirect('front_page')
    return wrap



