from django.http import HttpResponse
from django.shortcuts import redirect

from .models import User


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_new_student:
                return redirect('newStudentPage')
            elif request.user.is_bsit_student:
                return redirect('bsitStudentPage')
            elif request.user.is_bit_student:
                return redirect('bitStudentPage')
            elif request.user.is_staff:
                return redirect('faculty')
            else:
                return HttpResponse('You are not authorized to view this page')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            permissions = None
            if request.user.is_new_student:
                permissions = 'is_new_student'
            elif request.user.is_bsit_student:
                permissions = 'is_bsit_student'
            elif request.user.is_bit_student:
                permissions = 'is_bit_student'
            elif request.user.is_staff:
                permissions = 'is_staff'

            if permissions in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        permissions = None
        if request.user.is_new_student:
            permissions = 'is_new_student'
        elif request.user.is_bsit_student:
            permissions = 'is_bsit_student'
        elif request.user.is_bit_student:
            permissions = 'is_bit_student'
        elif request.user.is_staff:
            permissions = 'is_staff'

        if permissions == 'is_new_student':
            return redirect('newStudentPage')
        elif permissions == 'is_bsit_student':
            return redirect('bsitStudentPage')
        elif permissions == 'is_bit_student':
            return redirect('bitStudentPage')

        if permissions == 'is_staff':
            return view_func(request, *args, **kwargs)

    return wrapper_function
