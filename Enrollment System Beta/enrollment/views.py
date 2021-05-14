from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission

from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import LoginForm, RegisterForm, NewStudentChangeForm, BsitChangeForm, BitChangeForm, StudentSubjectForm, StudentSubjectForm2, UpdateStudentSubjectForm
from .models import User, SubjectForm, YearLevel, Semester, EnrollmentStatus, OfferedSubject

from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.


@unauthenticated_user
def registerPage(request):

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('mildde_name')
            last_name = form.cleaned_data.get('last_name')
            password_dispay = user.password
            template = render_to_string(
                'enrollment/user/email_template.html', {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'email': email, 'password': password_dispay})
            send_mail(
                'CTU-Ginatilan Enrollment System BETA',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )

            username = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'enrollment/user/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
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
            messages.info(
                request, 'The username/password you’ve entered is incorrect.')

    context = {}
    return render(request, 'enrollment/user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_staff'])
def facultyPage(request):

    return render(request, 'enrollment/faculty/template.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_new_student'])
def newStudentPage(request):
    # Future Works
    return render(request, 'enrollment/student/new/dashboard.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bsit_student'])
def bsitStudentPage(request):
    # Future Works
    return render(request, 'enrollment/student/old/bsit/dashboard.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bit_student'])
def bitStudentPage(request):
    # Future Works
    return render(request, 'enrollment/student/old/bit/dashboard.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_new_student'])
def displayNewStudentInfo(request):
    student_info = User.objects.all()

    context = {'student_info': student_info}
    return render(request, 'enrollment/student/new/view_info.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bsit_student'])
def displayBsitStudentInfo(request):
    student_info = User.objects.all()

    context = {'student_info': student_info}
    return render(request, 'enrollment/student/old/bsit/view_info.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bit_student'])
def displayBitStudentInfo(request):
    student_info = User.objects.all()

    context = {'student_info': student_info}
    return render(request, 'enrollment/student/old/bit/view_info.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_new_student'])
def newStudentUpdateInfo(request, pk):
    user = User.objects.get(id=pk)
    form = NewStudentChangeForm(instance=user)

    if request.method == 'POST':
        form = NewStudentChangeForm(request.POST, instance=user)
        if form.is_valid():
            user.new_student = True
            form.save()
            return redirect('displayNewStudentInfo')

    context = {'form': form}
    return render(request, "enrollment/student/new/update_info.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bsit_student'])
def bsitStudentUpdateInfo(request, pk):
    user = User.objects.get(id=pk)
    form = BsitChangeForm(instance=user)

    if request.method == 'POST':
        form = BsitChangeForm(request.POST, instance=user)
        if form.is_valid():
            user.new_student = True
            form.save()
            return redirect('displayBsitStudentInfo')

    context = {'form': form}
    return render(request, "enrollment/student/old/bsit/update_info.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['is_bit_student'])
def bitStudentUpdateInfo(request, pk):
    user = User.objects.get(id=pk)
    form = BitChangeForm(instance=user)

    if request.method == 'POST':
        form = BitChangeForm(request.POST, instance=user)
        if form.is_valid():
            user.new_student = True
            form.save()
            return redirect('displayBitStudentInfo')

    context = {'form': form}
    return render(request, "enrollment/student/old/bit/update_info.html", context)


def newStudentProfile(request):
    student_profile = User.objects.all()

    context = {'student_profile': student_profile}
    return render(request, "enrollment/student/new/profile.html", context)


def bsitStudentProfile(request):
    student_profile = User.objects.all()

    context = {'student_profile': student_profile}
    return render(request, "enrollment/student/old/bsit/profile.html", context)


def bitStudentProfile(request):
    student_profile = User.objects.all()

    context = {'student_profile': student_profile}
    return render(request, "enrollment/student/old/bit/profile.html", context)
# Subject Form


def studentSubjectForm1(request):

    form = StudentSubjectForm()
    if request.method == 'POST':
        form = StudentSubjectForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            form.save()

            return redirect('studentSubjectForm2')

    context = {'form': form}
    return render(request, "enrollment/student/new/subject_form1.html", context)


def studentSubjectForm2(request):
    subjects = SubjectForm.objects.all()

    context = {'subjects': subjects}
    return render(request, "enrollment/student/new/subject_form2.html", context)


def load_year_levels(request):
    course_id = request.GET.get('course')
    year_levels = YearLevel.objects.filter(
        course_id=course_id).order_by('name')
    context = {'year_levels': year_levels}
    return render(request, 'enrollment/subjects/year_level.html', context)


def load_semesters(request):
    year_level_id = request.GET.get('year_level')
    semesters = Semester.objects.filter(
        year_level_id=year_level_id).order_by('name')
    context = {'semesters': semesters}
    return render(request, 'enrollment/subjects/semester.html', context)


def load_enrollment_statuses(request):
    semester_id = request.GET.get('semester')
    enrollment_statuses = EnrollmentStatus.objects.filter(
        semester_id=semester_id).order_by('name')
    context = {'enrollment_statuses': enrollment_statuses}
    return render(request, 'enrollment/subjects/enrollment_status.html', context)
